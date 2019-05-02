import tw2.core as B,tw2.forms as A
class D(A.FormPage):
	title='GridLayout Validation'
	class child(A.Form):
		class child(A.GridLayout):repetitions=5;name=A.TextField(validator=B.Required);email=A.TextField(validator=B.EmailValidator())
if __name__=='__main__':import wsgiref.simple_server as C;C.make_server('',8000,B.make_middleware(controller_prefix='/')).serve_forever()