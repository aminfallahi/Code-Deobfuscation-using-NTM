'Main command.'
import os,sys
from pytest_bdd.scripts import main
A=os.path.dirname(__file__)
def B(monkeypatch,capsys):'Test if main commmand shows help when called without the subcommand.';A=monkeypatch;A.setattr(sys,'argv',['pytest-bdd']);A.setattr(sys,'exit',lambda x:x);main();C,B=capsys.readouterr();assert'usage: pytest-bdd [-h]'in B;assert'pytest-bdd: error:'in B