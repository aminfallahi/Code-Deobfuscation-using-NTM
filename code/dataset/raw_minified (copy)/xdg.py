'\nCreate an XDG function to get the config dir\n'
from __future__ import absolute_import
import os
def A():'\n    Check xdg locations for config files\n    ';A=os.getenv('XDG_CONFIG_HOME',os.path.expanduser('~/.config'));B=os.path.join(A,'salt');return B