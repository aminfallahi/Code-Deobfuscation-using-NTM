import json,tempfile as B,ui
C=[{'class':'Button','attributes':{'font_size':64,'title':'Tap me!'}}]
def D(view_list):
	with B.NamedTemporaryFile(suffix='.pyui')as A:json.dump(view_list,A);A.seek(0);return ui.load_view(A.name)
A=D(C)
A.action=lambda sender:sender.close()
A.present(hide_title_bar=True)