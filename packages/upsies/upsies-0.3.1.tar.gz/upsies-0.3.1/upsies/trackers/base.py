"""
Abstract base class for tracker APIs
"""

import abc
import argparse

from .. import jobs
from ..utils import cached_property, fs, signal, webdbs

import logging  # isort:skip
_log = logging.getLogger(__name__)


class TrackerConfigBase(dict):
    """
    Dictionary with default values that are defined by the subclass

    The keys ``announce``, ``source`` and ``exclude`` always exist.
    """

    _defaults = {
        'source'     : '',
        'exclude'    : [],
        'add-to'     : '',
        'copy-to'    : '',
    }

    defaults = {}
    """Default values"""

    def __new__(cls, config={}):
        combined_defaults = {**cls._defaults, **cls.defaults}
        for k in config:
            if k not in combined_defaults:
                raise TypeError(f'Unknown option: {k!r}')
        obj = super().__new__(cls)
        obj.update(combined_defaults)
        obj.update(config)
        return obj

    # If the config is passed as config={...}, super().__init__() will interpret
    # as a key-value pair that ends up in the config.
    def __init__(cls, *args, **kwargs):
        pass


class TrackerJobsBase(abc.ABC):
    """
    Base class for tracker-specific :class:`jobs <upsies.jobs.base.JobBase>`

    Jobs are instantiated on demand by an instance of this class, which means
    all arguments for all jobs must be given to this class during instantiation.

    Job instances are provided as :func:`~functools.cached_property`, i.e. jobs
    are created only once per session.

    Subclasses that need to run background tasks (e.g. with
    :func:`asyncio.ensure_future`) should attach a callback to them with
    :meth:`~.asyncio.Task.add_done_callback` that catches expected exceptions
    and pass them to :meth:`warn`, :meth:`error` or :meth:`exception`.

    This base class defines general-purpose jobs that can be used by subclasses
    by returning them in their :attr:`jobs_before_upload` or
    :attr:`jobs_after_upload` attributes.

    For a description of the arguments see the corresponding properties.
    """

    def __init__(self, *, content_path, tracker, image_host, bittorrent_client,
                 torrent_destination, common_job_args, cli_args=None):
        self._content_path = content_path
        self._tracker = tracker
        self._image_host = image_host
        self._bittorrent_client = bittorrent_client
        self._torrent_destination = torrent_destination
        self._common_job_args = common_job_args
        self._cli_args = cli_args or argparse.Namespace()
        self._signal = signal.Signal('warning', 'error', 'exception')
        self._background_tasks = []

    @property
    def cli_args(self):
        """
        Command line arguments as :class:`argparse.Namespace` object from
        initialization
        """
        return self._cli_args

    @property
    def content_path(self):
        """Path to the content to generate metadata for"""
        return self._content_path

    @property
    def tracker(self):
        """:class:`~.trackers.base.TrackerBase` subclass"""
        return self._tracker

    @property
    def signal(self):
        """
        :class:`~.signal.Signal` instance with the signals ``warning``, ``error``
        and ``exception``
        """
        return self._signal

    def warn(self, warning):
        """
        Emit ``warning`` signal (see :attr:`signal`)

        Emit a warning for any non-critical issue that the user can choose to
        ignore or fix.
        """
        self.signal.emit('warning', warning)

    def error(self, error):
        """
        Emit ``error`` signal (see :attr:`signal`)

        Emit an error for any critical but expected issue that can't be
        recovered from (e.g. I/O error).
        """
        self.signal.emit('error', error)

    def exception(self, exception):
        """
        Emit ``exception`` signal (see :attr:`signal`)

        Emit an exception for any critical and unexpected issue that should be
        reported as a bug.
        """
        self.signal.emit('exception', exception)

    @property
    def image_host(self):
        """:class:`~.utils.imghosts.base.ImageHostBase` instance or `None`"""
        return self._image_host

    @property
    def bittorrent_client(self):
        """:class:`~.utils.btclients.base.ClientApiBase` instance or `None`"""
        return self._bittorrent_client

    @property
    def torrent_destination(self):
        """Path to copy the generated torrent file to or `None`"""
        return self._torrent_destination

    @property
    def common_job_args(self):
        """Keyword arguments as a dictionary that are passed to all jobs"""
        return self._common_job_args

    @property
    @abc.abstractmethod
    def jobs_before_upload(self):
        """
        Sequence of jobs that need to finish before :meth:`~.TrackerBase.upload` can
        be called
        """

    @cached_property
    def jobs_after_upload(self):
        """
        Sequence of jobs that are started after :meth:`~.TrackerBase.upload`
        finished

        .. note:: Jobs returned by this class should have
                  :attr:`~.JobBase.autostart` set to False or they will be
                  started before submission is attempted.

        By default, this returns :attr:`add_torrent_job` and
        :attr:`copy_torrent_job`.
        """
        return (
            self.add_torrent_job,
            self.copy_torrent_job,
        )

    @property
    def submission_ok(self):
        """
        Whether the created metadata should be submitted

        The base class implementation simply returns `True` if all
        :attr:`jobs_before_upload` have an :attr:`~.base.JobBase.exit_code` of
        ``0`` or a falsy :attr:`~.base.JobBase.is_enabled` value.

        Subclasses should always call the parent class implementation to ensure
        all metadata was created successfully.
        """
        enabled_jobs_before_upload = tuple(
            job for job in self.jobs_before_upload
            if job.is_enabled
        )
        return (
            bool(enabled_jobs_before_upload)
            and all(job.exit_code == 0
                    for job in enabled_jobs_before_upload)
        )

    @cached_property
    def create_torrent_job(self):
        """:class:`~.jobs.torrent.CreateTorrentJob` instance"""
        return jobs.torrent.CreateTorrentJob(
            content_path=self.content_path,
            tracker=self.tracker,
            **self.common_job_args,
        )

    @cached_property
    def add_torrent_job(self):
        """:class:`~.jobs.torrent.AddTorrentJob` instance"""
        if self.bittorrent_client:
            add_torrent_job = jobs.torrent.AddTorrentJob(
                autostart=False,
                client=self.bittorrent_client,
                download_path=fs.dirname(self.content_path),
                **self.common_job_args,
            )
            # Pass CreateTorrentJob output to AddTorrentJob input.
            self.create_torrent_job.signal.register('output', add_torrent_job.enqueue)
            # Tell AddTorrentJob to finish the current upload and then finish.
            self.create_torrent_job.signal.register('finished', self.finalize_add_torrent_job)
            return add_torrent_job

    def finalize_add_torrent_job(self, _):
        self.add_torrent_job.finalize()

    @cached_property
    def copy_torrent_job(self):
        """:class:`~.jobs.torrent.CopyTorrentJob` instance"""
        if self.torrent_destination:
            copy_torrent_job = jobs.torrent.CopyTorrentJob(
                autostart=False,
                destination=self.torrent_destination,
                **self.common_job_args,
            )
            # Pass CreateTorrentJob output to CopyTorrentJob input.
            self.create_torrent_job.signal.register('output', copy_torrent_job.enqueue)
            # Tell CopyTorrentJob to finish when CreateTorrentJob is done.
            self.create_torrent_job.signal.register('finished', self.finalize_copy_torrent_job)
            return copy_torrent_job

    def finalize_copy_torrent_job(self, _):
        self.copy_torrent_job.finalize()

    @cached_property
    def release_name_job(self):
        """:class:`~.jobs.release_name.ReleaseNameJob` instance"""
        return jobs.release_name.ReleaseNameJob(
            content_path=self.content_path,
            **self.common_job_args,
        )

    @cached_property
    def imdb_job(self):
        """:class:`~.jobs.webdb.WebDbSearchJob` instance"""
        imdb_job = jobs.webdb.WebDbSearchJob(
            content_path=self.content_path,
            db=webdbs.webdb('imdb'),
            **self.common_job_args,
        )
        # Update release name with IMDb data
        imdb_job.signal.register('output', self.release_name_job.fetch_info)
        return imdb_job

    @cached_property
    def tmdb_job(self):
        """:class:`~.jobs.webdb.WebDbSearchJob` instance"""
        return jobs.webdb.WebDbSearchJob(
            content_path=self.content_path,
            db=webdbs.webdb('tmdb'),
            **self.common_job_args,
        )

    @cached_property
    def tvmaze_job(self):
        """:class:`~.jobs.webdb.WebDbSearchJob` instance"""
        return jobs.webdb.WebDbSearchJob(
            content_path=self.content_path,
            db=webdbs.webdb('tvmaze'),
            **self.common_job_args,
        )

    screenshots = 2
    """Number of screenshots to make"""

    @cached_property
    def screenshots_job(self):
        """
        :class:`~.jobs.screenshots.ScreenshotsJob` instance

        The number of screenshots to make is taken from the "--screenshots" CLI
        argument, if present and non-falsy, and defaults to :attr:`screenshots`.
        """
        return jobs.screenshots.ScreenshotsJob(
            content_path=self.content_path,
            count=getattr(self.cli_args, 'screenshots', None) or self.screenshots,
            **self.common_job_args,
        )

    @cached_property
    def upload_screenshots_job(self):
        """:class:`~.jobs.imghost.ImageHostJob` instance"""
        if self.image_host:
            imghost_job = jobs.imghost.ImageHostJob(
                imghost=self.image_host,
                **self.common_job_args,
            )
            # Timestamps are calculated in a subprocess, we have to wait for
            # that until we can set the number of expected screenhots.
            self.screenshots_job.signal.register(
                'timestamps',
                lambda timestamps: imghost_job.set_images_total(len(timestamps)),
            )
            # Pass ScreenshotsJob's output to ImageHostJob input.
            self.screenshots_job.signal.register('output', imghost_job.enqueue)
            # Tell imghost_job to finish the current upload and then finish.
            self.screenshots_job.signal.register('finished', self.finalize_upload_screenshots_job)
            return imghost_job

    def finalize_upload_screenshots_job(self, _):
        self.upload_screenshots_job.finalize()

    @cached_property
    def mediainfo_job(self):
        """:class:`~.jobs.mediainfo.MediainfoJob` instance"""
        return jobs.mediainfo.MediainfoJob(
            content_path=self.content_path,
            **self.common_job_args,
        )

    @cached_property
    def scene_check_job(self):
        """:class:`~.jobs.scene.SceneCheckJob` instance"""
        return jobs.scene.SceneCheckJob(
            content_path=self.content_path,
            **self.common_job_args,
        )


class TrackerBase(abc.ABC):
    """
    Base class for tracker-specific operations, e.g. uploading

    :param config: User configuration options for this tracker,
        e.g. authentication details, announce URL, etc
    :type config: :attr:`TrackerConfig`
    :param cli_args: Command line arguments as defined by
        :attr:`argument_defintions`
    :type cli_args: :class:`argparse.Namespace`
    """

    @property
    @abc.abstractmethod
    def TrackerJobs(self):
        """Subclass of :class:`TrackerJobsBase`"""

    @property
    @abc.abstractmethod
    def TrackerConfig(self):
        """Subclass of :class:`TrackerConfigBase`"""

    def __init__(self, config=None, cli_args=None):
        self._config = config or {}
        self._cli_args = cli_args or argparse.Namespace()

    argument_definitions = {}
    """CLI argument definitions (see :attr:`.CommandBase.argument_definitions`)"""

    @property
    def cli_args(self):
        """
        Command line arguments as :class:`argparse.Namespace` object from
        initialization
        """
        return self._cli_args

    @property
    @abc.abstractmethod
    def name(self):
        """Lower-case tracker name abbreviation for internal use"""

    @property
    @abc.abstractmethod
    def label(self):
        """User-facing tracker name abbreviation"""

    @property
    def config(self):
        """:attr:`~.TrackerBase.TrackerConfig` object from initialization argument"""
        return self._config

    @abc.abstractmethod
    async def login(self):
        """Start user session"""

    @abc.abstractmethod
    async def logout(self):
        """End user session"""

    @property
    @abc.abstractmethod
    def is_logged_in(self):
        """Whether a user session is active"""

    @abc.abstractmethod
    async def get_announce_url(self):
        """Get announce URL from tracker website"""

    @abc.abstractmethod
    async def upload(self, tracker_jobs):
        """
        Upload torrent and other metadata from jobs

        :param TrackerJobsBase tracker_jobs: :attr:`TrackerJobs` instance
        """
