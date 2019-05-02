from sphinx import addnodes as C
def A(app,doctree):
	A=app;B=A.builder.env.temp_data['docname']
	if A.builder.env.metadata[B].get('tocdepth',0)!=0:
		for D in doctree.traverse(C.toctree):A.builder.env.note_toctree(B,D)
def B(app):app.connect('doctree-read',A)