'\nsentry.utils.compat\n~~~~~~~~~~~~~~~~~~~\n\nContains compatibility imports (generally c-module replacements)\n\n:copyright: (c) 2010 by the Sentry Team, see AUTHORS for more details.\n:license: BSD, see LICENSE for more details.\n'
B=ImportError
try:import cPickle as A
except B:import pickle as A
try:import cmath as math
except B:import math