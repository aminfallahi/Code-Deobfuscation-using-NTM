from flask import Blueprint as A,render_template as B
from .  import route
C=A('shanks',__name__)
@route(C,'/')
def D():'Returns the index interface.';return B('index.html')