import mock as B
from elodie.dependencies import get_exiftool as A
@B.patch('elodie.dependencies.find_executable')
@B.patch('elodie.dependencies.os')
def C(mock_os,mock_find_executable):F=True;E=None;D='/path/to/exiftool';C=mock_find_executable;B=mock_os;C.return_value=D;assert A()==D;C.return_value=E;B.path.isfile.return_value=F;B.path.access.return_value=F;assert A()=='/usr/local/bin/exiftool';B.path.isfile.return_value=False;assert A()is E