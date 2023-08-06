__version__ = '0.1.0'

import sys

from . import logging
from ._stubs import AudioFrame, CodecContext, VideoFrame


def install_as_av():
    if 'av' not in sys.modules:
        sys.modules['av'] = sys.modules['aiortc_pyav_stub']
    elif sys.modules['av'] != sys.modules['aiortc_pyav_stub']:
        raise RuntimeError(
            "The 'av' module has already been imported. Can't install stub module."
        )
