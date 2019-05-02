from flask_wtf import Form
from flask_wtf.file import FileField as A,FileRequired as B
from wtforms import SubmitField as C
class D(Form):upload=A(label='Select a file to upload',validators=[B()]);submit=C(label='Engage!')