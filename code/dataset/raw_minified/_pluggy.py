'\nimports symbols from vendored "pluggy" if available, otherwise\nfalls back to importing "pluggy" from the default namespace.\n'
try:from _pytest.vendored_packages.pluggy import *;from _pytest.vendored_packages.pluggy import __version__
except ImportError:from pluggy import *;from pluggy import __version__