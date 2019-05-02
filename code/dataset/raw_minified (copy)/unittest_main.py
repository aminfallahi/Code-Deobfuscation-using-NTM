'Main entry point'
import sys as A
if A.argv[0].endswith('__main__.py'):import os.path;B=os.path.basename(A.executable);A.argv[0]=B+' -m unittest';del os
C=True
from unittest.main import main,TestProgram
main(module=None)