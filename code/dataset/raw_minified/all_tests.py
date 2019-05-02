__author__='Robert Meyer'
from pypet.tests.testutils.ioutils import run_suite as A,discover_tests as B,TEST_IMPORT_ERROR as C,parse_args as D
if __name__=='__main__':E=D();F=B(predicate=lambda class_name,test_name,tags:class_name!=C);A(suite=F,**E)