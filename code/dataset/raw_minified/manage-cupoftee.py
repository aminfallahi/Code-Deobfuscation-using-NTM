'\n    Manage Cup Of Tee\n    ~~~~~~~~~~~~~~~~~\n\n    Manage the cup of tee application.\n\n    :copyright: (c) 2009 by the Werkzeug Team, see AUTHORS for more details.\n    :license: BSD, see LICENSE for more details.\n'
from werkzeug import script as A
def B():from cupoftee import make_app as A;return A('/tmp/cupoftee.db')
C=A.make_runserver(B)
A.run()