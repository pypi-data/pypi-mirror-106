"""hydroMT plugin for wflow models."""

from os.path import join, dirname, abspath

__version__ = "0.1.1"

try:
    import pcraster as pcr

    HAS_PCRASTER = True
except ImportError:
    HAS_PCRASTER = False

DATADIR = join(dirname(abspath(__file__)), "data")
