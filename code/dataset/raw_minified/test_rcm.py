from nose.tools import *
from networkx.utils import reverse_cuthill_mckee_ordering
import networkx as nx
def test_reverse_cuthill_mckee():G=nx.Graph([(0,3),(0,5),(1,2),(1,4),(1,6),(1,9),(2,3),(2,4),(3,5),(3,8),(4,6),(5,6),(5,7),(6,7)]);rcm=list(reverse_cuthill_mckee_ordering(G,start=0));assert_equal(rcm,[9,1,4,6,7,2,8,5,3,0]);rcm=list(reverse_cuthill_mckee_ordering(G));assert_equal(rcm,[0,8,5,7,3,6,4,2,1,9])