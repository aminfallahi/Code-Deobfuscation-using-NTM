'\nBackwards-compatible for django-uni-form versions previous to 0.9.0\nHelpers.py was split into 3 different files in version 0.9.0: helper.py, layout.py and util.py\nIn order to keep former imports working this file is kept. \n\nThis usage will be deprecated and will be removed for django-uni-form 1.1.0\n'
import warnings
warnings.warn('Importing from helpers is deprecated; import from helper or layout instead.',DeprecationWarning)
from helper import *
from layout import *