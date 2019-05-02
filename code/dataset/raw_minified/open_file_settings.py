import sublime as B,sublime_plugin as A,os.path
class C(A.WindowCommand):
	def run(A):C=A.window.active_view();D,F=os.path.splitext(os.path.basename(C.settings().get('syntax')));E=os.path.join(B.packages_path(),'User');A.window.open_file(os.path.join(E,D+'.sublime-settings'))
	def is_enabled(A):return A.window.active_view()!=None