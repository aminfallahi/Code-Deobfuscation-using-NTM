'\nA data grid can be achieved using a GridLayout that contains LabelField widgets.\n'
import tw2.core as B,tw2.forms as A
class D(B.Page):
	title='Data Grid'
	class child(A.GridLayout):extra_reps=0;id=A.LinkField(link='detail?id=$',text='View',label=None);a=A.LabelField();b=A.LabelField()
	def fetch_data(A,req):D='b';C='a';B='id';A.value=[{B:1,C:'paj',D:'bob'},{B:2,C:'joe',D:'jill'}]
if __name__=='__main__':import wsgiref.simple_server as C;C.make_server('',8000,B.make_middleware(controller_prefix='/')).serve_forever()