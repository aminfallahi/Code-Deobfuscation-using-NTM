'\nCreate an inbox.\n'
from diffscuss.mailbox.common import get_inbox_name,get_inbox_path as B,check_inited as C,mkdir_for_keeps as D
def A(args):A=args;C(A.git_exe);E=A.inbox;F=B(E,A.git_exe);D(F)