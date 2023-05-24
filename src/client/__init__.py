from ..configuration import Configuration
from .instrument_client import *
from .timeframe_client import *


def SetDefaultHost(host: str):
    Configuration.DEFAULT_HOST = host
