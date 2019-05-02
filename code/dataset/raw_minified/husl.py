'\nHandle loading husl package from system or from the bundled copy\n'
try:from ._bundled.husl import *
except ImportError:from husl import *