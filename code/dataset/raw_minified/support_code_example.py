from __future__ import absolute_import,print_function
import sys
sys.path.insert(0,'..')
import inline_tools as A
B='\n               PyObject* length(std::string a)\n               {\n                   int l = a.length();\n                   return PyInt_FromLong(l);\n               }\n               '
D='some string'
C=A.inline('return_val = length(a);',['a'],support_code=B)
print(C)