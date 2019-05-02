'\n    test_ext_ifconfig\n    ~~~~~~~~~~~~~~~~~\n\n    Test sphinx.ext.ifconfig extension.\n\n    :copyright: Copyright 2007-2016 by the Sphinx team, see AUTHORS.\n    :license: BSD, see LICENSE for details.\n'
import re
from util import with_app as A
@A(testroot='ext-ifconfig')
def B(app,status,warning):app.builder.build_all()