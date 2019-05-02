from __future__ import absolute_import
from .simulator import *
def is_available():'Returns a boolean to indicate the availability of a CUDA GPU.\n    ';return True
def cuda_error():'Returns None or an exception if the CUDA driver fails to initialize.\n    ';return None