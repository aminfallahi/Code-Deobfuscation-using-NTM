'\nSets up the terminal color scheme.\n'
from django.core.management import color as C
from django.utils import termcolors as B
def A():
	D='bold';A=C.color_style()
	if C.supports_color():A.URL=B.make_style(fg='green',opts=(D,));A.MODULE=B.make_style(fg='yellow');A.MODULE_NAME=B.make_style(opts=(D,));A.URL_NAME=B.make_style(fg='red')
	return A