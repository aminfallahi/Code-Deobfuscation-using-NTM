from pygments.lexers import get_all_lexers as B
from .  import blueprint as A
@A.route('/')
def C():
	from flask import render_template as C;A=[]
	for D in B():A.extend(D[3])
	return C('index.html',contenttypes=A)