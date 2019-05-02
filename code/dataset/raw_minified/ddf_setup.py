from django_dynamic_fixture import N,DDFLibrary as A
from django_dynamic_fixture.models_test import ModelForDDFSetup as B
C=A()
A.instance=C
N(B,integer=1000,shelve='test1')
N(B,integer=1001,shelve=True)
N(B,integer=1002,shelve='test2')
A.instance=A()