'\nTests for the proxy support in pip.\n'
import pip
from tests.lib import SRC_DIR as A
from tests.lib.path import Path
def B():'\n    Check we are importing pip from the right place.\n\n    ';assert Path(pip.__file__).folder.folder.abspath==A