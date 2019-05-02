import angr,logging as B,os
G=B.getLogger('angr_tests')
C=str(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../../binaries/tests'))
A=angr.Project(os.path.join(C,'x86_64/track_user_input'))
D=A.loader.main_bin.get_symbol('main').addr
E=4195440
F=A.analyses.CFG(keep_state=True)
H=F.get_paths(D,E)