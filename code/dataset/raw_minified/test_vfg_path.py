import angr,logging as A,os
D=A.getLogger('angr_tests')
B=str(os.path.join(os.path.dirname(os.path.realpath(__file__)),'../../binaries/tests'))
def C():A=angr.Project(os.path.join(B,'x86_64/track_user_input'));C=A.loader.main_bin.get_symbol('main').addr;D=4195809;E=A.analyses.VFG(context_sensitivity_level=1,interfunction_level=3);F=E.get_paths(C,D)
if __name__=='__main__':C()