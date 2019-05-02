from collections import namedtuple as C
import json,os
D=C('Language','english native iso639_1')
E=os.path.join(os.path.dirname(__file__),'languages.json')
A=json.loads(open(E,'r').read())
F={}
for B in A:F[B]=D(A[B]['english'],A[B]['native'],A[B]['iso639_1'])