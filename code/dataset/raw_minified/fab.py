from depl.deploy._utils import lazy
def deploy(string):python_code='from fabric.api import *\n'+string;return _run(python_code),
@lazy
def _run(python_code):exec(python_code)