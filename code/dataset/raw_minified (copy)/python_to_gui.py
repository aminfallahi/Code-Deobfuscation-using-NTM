from sample_app import app as A
A.html='<html></html>'
A.template='./index.html',{'template_variable_name':'value'}
A.evaluate_javascript("alert('Hello from back-end')")