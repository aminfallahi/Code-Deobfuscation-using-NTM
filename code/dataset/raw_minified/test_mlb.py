import os,sys
from nose.tools import eq_
import vcr
A=os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,os.path.join(A,'../../limbo/plugins'))
from mlb import on_message as B
def C():
	with vcr.use_cassette('test/fixtures/mlb_basic.yaml'):A=B({'text':'!mlb Red Sox'},None);assert'Boston Red Sox'in A