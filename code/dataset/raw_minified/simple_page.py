from flask import Blueprint as B,render_template as C,abort
from jinja2 import TemplateNotFound as D
A=B('simple_page',__name__,template_folder='templates')
@A.route('/',defaults={'page':'index'})
@A.route('/<page>')
def E(page):
	try:return C('pages/%s.html'%page)
	except D:abort(404)