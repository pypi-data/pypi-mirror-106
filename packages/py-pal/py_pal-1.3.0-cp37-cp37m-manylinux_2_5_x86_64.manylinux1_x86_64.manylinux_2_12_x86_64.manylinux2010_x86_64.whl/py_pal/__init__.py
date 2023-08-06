__version__ = '1.3.0'

import sys
from platform import python_implementation

assert sys.version_info >= (3, 7)
assert python_implementation() == 'CPython'
