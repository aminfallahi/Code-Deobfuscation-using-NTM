import sublime_plugin as A
class B(A.WindowCommand):
	def run(A):
		if A.window.project_file_name():A.window.run_command('close_workspace')
		else:
			A.window.run_command('close_all')
			if any([B.is_dirty()for B in A.window.views()]):return
			A.window.run_command('close_project')
		A.window.run_command('close_window')