import pytest as A
from app import create_app as B
@A.mark.parametrize('flask_config',['production','development'])
def C(flask_config):B(flask_config=flask_config)