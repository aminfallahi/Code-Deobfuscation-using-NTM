' Testing loading of gifti file\n\nThe file is ``test_1`` because we are testing a bug where, if we try to load a\nfile before instantiating some Gifti objects, loading fails with an\nAttributeError (see: https://github.com/nipy/nibabel/issues/392).\n\nThus, we have to run this test before the other gifti tests to catch the gifti\ncode unprepared.\n'
from nibabel import load
from .test_parse_gifti_fast import DATA_FILE3 as A
def B():load(A)