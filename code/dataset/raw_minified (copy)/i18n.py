class A:
	def __init__(A,localizer):A.t=localizer
	def gettext(A,string):return A.t.translate(string)
	def ngettext(A,single,plural,string):return A.t.pluralize(single,plural,string)