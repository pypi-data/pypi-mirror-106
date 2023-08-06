"""The analysis server. Process raw image to PDF."""
import typing as tp

from area_detector_handlers.handlers import AreaDetectorTiffHandler
from bluesky.callbacks.zmq import Publisher
from databroker.v1 import Broker
from event_model import RunRouter
from ophyd.sim import NumpySeqHandler

import pdfstream.io as io
from pdfstream.callbacks.analysis import AnalysisConfig, VisConfig, ExportConfig, AnalysisStream, Exporter, \
    Visualizer
from pdfstream.callbacks.calibration import CalibrationConfig, Calibration
from pdfstream.servers import CONFIG_DIR, ServerNames
from pdfstream.servers.base import ServerConfig, find_cfg_file, BaseServer, StartStopCallback


class XPDConfig(AnalysisConfig, VisConfig, ExportConfig, CalibrationConfig):
    """The configuration for the xpd data reduction. It consists of analysis, visualization and exportation."""

    def __init__(self, *args, **kwargs):
        super(XPDConfig, self).__init__(*args, **kwargs)
        self.add_section("PUBLISH TO")
        self.add_section("FUNCTIONALITY")

    @property
    def an_db(self) -> str:
        return self.get("DATABASE", "an_db", fallback="")

    @property
    def publisher_config(self) -> dict:
        host = self.get("PUBLISH TO", "host", fallback="localhost")
        port = self.getint("PUBLISH TO", "port", fallback=5567)
        prefix = self.get("PUBLISH TO", "prefix", fallback="an").encode()
        return {
            "address": (host, port),
            "prefix": prefix
        }

    @property
    def functionality(self) -> dict:
        return {
            "do_calibration": self.getboolean("FUNCTIONALITY", "do_calibration", fallback=True),
            "dump_to_db": self.getboolean("FUNCTIONALITY", "dump_to_db", fallback=True),
            "export_files": self.getboolean("FUNCTIONALITY", "export_files", fallback=True),
            "visualize_data": self.getboolean("FUNCTIONALITY", "visualize_data", fallback=True),
            "send_messages": self.getboolean("FUNCTIONALITY", "send_messages", fallback=False)
        }


class XPDServerConfig(XPDConfig, ServerConfig):
    """The configuration for xpd server."""
    pass


class XPDServer(BaseServer):
    """The server of XPD data analysis. It is a live dispatcher with XPDRouter subscribed."""
    def __init__(self, config: XPDServerConfig):
        super(XPDServer, self).__init__(config.address, prefix=config.prefix)
        self.subscribe(StartStopCallback())
        self.subscribe(XPDRouter(config))


def make_and_run(
    cfg_file: str = None,
    *,
    suppress_warning: bool = True,
    test_mode: bool = False
):
    """Run the xpd data reduction server.

    The server will receive message from proxy and process the data in the message. The processed data will be
    visualized and exported to database and the file system.

    Parameters
    ----------
    cfg_file :
        The path to configuration .ini file. The default path is "~/.config/acq/xpd_server.ini".

    suppress_warning :
        If True, all warning will be suppressed. Turn it to False when running in a test.

    test_mode :
        If True, just create a server but not start. Used for test.
    """
    if suppress_warning:
        import warnings
        warnings.simplefilter("ignore")
    if not cfg_file:
        cfg_file = find_cfg_file(CONFIG_DIR, ServerNames.xpd)
    config = XPDServerConfig()
    config.read(cfg_file)
    server = XPDServer(config)
    if config.functionality["visualize_data"] and not test_mode:
        server.install_qt_kicker()
    if not test_mode:
        server.start()


class XPDRouter(RunRouter):
    """A router that contains the callbacks for the xpd data reduction."""

    def __init__(self, config: XPDConfig):
        factory = XPDFactory(config)
        super(XPDRouter, self).__init__(
            [factory],
            handler_registry={
                "NPY_SEQ": NumpySeqHandler,
                "AD_TIFF": AreaDetectorTiffHandler
            }
        )


class XPDFactory:
    """The factory to generate callback for xpd data reduction."""

    def __init__(self, config: XPDConfig):
        self.config = config
        self.functionality = self.config.functionality
        self.analysis = [AnalysisStream(config)]
        self.calibration = [Calibration(config)] if self.functionality["do_calibration"] else []
        if self.functionality["dump_to_db"] and self.config.an_db:
            db = Broker.named(self.config.an_db)
            self.analysis[0].subscribe(db.insert)
        if self.functionality["export_files"]:
            self.analysis[0].subscribe(Exporter(config))
        if self.functionality["visualize_data"]:
            self.analysis[0].subscribe(Visualizer(config))
        if self.functionality["send_messages"]:
            self.analysis[0].subscribe(Publisher(**self.config.publisher_config))

    def __call__(self, name: str, doc: dict) -> tp.Tuple[list, list]:
        if name == "start":
            if doc.get(self.config.dark_identifier):
                # dark frame run
                io.server_message("Ignore dark frame.")
                return [], []
            elif doc.get(self.config.calib_identifier):
                # calibration run
                io.server_message("Start calibration.")
                return self.calibration, []
            else:
                # light frame run
                io.server_message("Start data reduction.")
                return self.analysis, []
        return [], []
