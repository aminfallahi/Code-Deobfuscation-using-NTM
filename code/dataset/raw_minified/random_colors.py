from phue import Bridge as C
import random as A
D=C()
E=D.get_light_objects()
for B in E:B.brightness=254;B.xy=[A.random(),A.random()]