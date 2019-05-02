from jinja2 import Template as A
B='template.txt'
C={'iternum':32,'depth':4}
def D(filename,temp_dict):B=open(filename,'r').read();C=A(B);D=C.render(temp_dict);return D
print(D(B,C))