E='password'
D='username'
from taiga_ncurses.ui import views as A
def B():B=A.auth.LoginView(D,E);C='Hulk Hogan';B._username_editor.set_edit_text(C);assert B.username==C
def C():B=A.auth.LoginView(D,E);C='1234567890';B._password_editor.set_edit_text(C);assert B.password==C