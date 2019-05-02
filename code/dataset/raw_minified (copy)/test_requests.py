import pytest as A
@A.mark.skipif
def B(script):A=script.pip('--timeout','0.01','install','-vvv','INITools',expect_error=True);assert'Could not fetch URL https://pypi.python.org/simple/INITools/: timed out'in A.stdout;assert'Could not fetch URL https://pypi.python.org/simple/: timed out'in A.stdout