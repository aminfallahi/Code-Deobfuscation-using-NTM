'\nImplementation of the command-line I{pyflakes} tool.\n'
from __future__ import absolute_import
__all__=['check','checkPath','checkRecursive','iterSourceCode','main']
from pyflakes.api import check,checkPath,checkRecursive,iterSourceCode,main