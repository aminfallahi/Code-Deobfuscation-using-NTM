B=ImportError
try:import urlparse as parse
except B:from urllib import parse
try:import __builtin__ as A
except B:import builtins as A
import example1