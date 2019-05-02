'\nThis is a module that imports the *standard library* unittest,\ndespite there being a local "unittest" module. It specifies that it\nwants the stdlib one with the ``absolute_import`` __future__ import.\n\nThe twisted equivalent of this module is ``twisted.trial._synctest``.\n'
from __future__ import absolute_import
import unittest as A
class B(A.TestCase):0