import mahotas.demos
from os import path as A
def B():assert A.exists(mahotas.demos.image_path('luispedro.jpg'));assert not A.exists(mahotas.demos.image_path('something-that-does-not-exist'))