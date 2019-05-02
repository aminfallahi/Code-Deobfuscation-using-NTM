_B='tests/sample.ini'
_A='threadserver.run_dir'
from nose.tools import *
from lust import config
def test_load_ini_file():settings=config.load_ini_file(_B);assert_equal(settings[_A],'/var/run/threadserver')
def test_load_ini_file_defaults():A='/var/other';settings=config.load_ini_file(_B,defaults={_A:A});assert_equal(settings[_A],A)