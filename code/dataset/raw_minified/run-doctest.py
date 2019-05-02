import argparse as C,doctest as A
B=C.ArgumentParser(description='Run a test by name')
B.add_argument('test_name')
D=B.parse_args()
A.testfile(D.test_name,optionflags=A.REPORT_ONLY_FIRST_FAILURE)