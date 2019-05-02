G=False
F=True
import jinja2 as C
from jinja2 import Environment as B
A=C.FileSystemLoader(searchpath='/')
D=''
B(loader=A,load=A,autoescape=F)
E=C.Environment(autoescape=F,loader=A)
B(loader=A,load=A,autoescape=D)
E=C.Environment(autoescape=G,loader=A)
B(loader=A,load=A,autoescape=G)
B(loader=A,load=A)