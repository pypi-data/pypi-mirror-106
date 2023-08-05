import os

os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "bcm"

from .cloister import *
from .galaxy import *
from .rocket import *
from .version import VERSION

__version__ = VERSION
