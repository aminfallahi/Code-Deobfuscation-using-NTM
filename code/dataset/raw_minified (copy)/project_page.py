from jsl import BooleanField as A,Document as B,IntField as C
class D(B):project_id=C(minimum=0,required=True);archived=A();include_stories=A()
E=D.get_schema()
F=None