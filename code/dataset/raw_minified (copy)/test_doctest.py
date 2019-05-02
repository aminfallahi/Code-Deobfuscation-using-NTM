import pytest
from hamcrest import assert_that as A,contains as B,all_of,has_entry,has_property as C,has_properties
def D(report_for):D=report_for("\n    def hello_world():\n        '''\n        >>> hello_world()\n        'hello world'\n        '''\n        return 'hello world'\n    ",['--doctest-modules']);A(D.findall('.//test-case'),B(C('description','[doctest] test_doctests.hello_world')))