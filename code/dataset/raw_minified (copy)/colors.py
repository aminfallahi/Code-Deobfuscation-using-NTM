from fabric import colors as B
from fabric.api import env
def A(color,msg):
	if env.no_color:return msg
	return getattr(B,color)(msg)
C=lambda msg:A('red',msg)
D=lambda msg:A('green',msg)
E=lambda msg:A('yellow',msg)