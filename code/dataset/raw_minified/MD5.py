__revision__='$Id$'
from .md5 import *
from .  import md5
if hasattr(md5,'digestsize'):digest_size=digestsize;del digestsize
del md5