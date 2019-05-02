C='.'
import htmlPy as B,os
A=B.AppGUI(title='htmlPy Quickstart',maximized=True)
A.template_path=os.path.abspath(C)
A.static_path=os.path.abspath(C)
A.template='index.html',{'username':'htmlPy_user'}
A.start()