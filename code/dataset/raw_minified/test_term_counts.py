from textplot.text import Text
from collections import OrderedDict as A
def B():'\n    term_counts() should return a map of term -> count.\n    ';B=Text('aa bb bb cc cc cc');assert B.term_counts()==A([('cc',3),('bb',2),('aa',1)])