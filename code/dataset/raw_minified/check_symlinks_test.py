import os,pytest as A
from pre_commit_hooks.check_symlinks import check_symlinks as B
from testing.util import get_resource_path as C
@A.mark.xfail(os.name=='nt',reason='No symlink support on windows')
@A.mark.parametrize(('filename','expected_retval'),(('broken_symlink',1),('working_symlink',0)))
def D(filename,expected_retval):A=B([C(filename)]);assert A==expected_retval