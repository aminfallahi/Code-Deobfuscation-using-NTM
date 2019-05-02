'\nAn example of how to customize the keyboard shortcuts.\nBy default mpldatacursor will use "t" to toggle interactivity and "d" to\nhide/delete annotation boxes.\n'
import matplotlib.pyplot as A
from mpldatacursor import datacursor as C
D,B=A.subplots()
B.plot(range(10),'bo-')
B.set_title('Press "e" to enable/disable the datacursor\nPress "h" to hide any annotation boxes')
E=C(keybindings=dict(hide='h',toggle='e'))
A.show()