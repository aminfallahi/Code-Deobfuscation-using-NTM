from nose.tools import assert_equal as C,raises as B
import networkx as A
def D():B=A.Graph();B.add_edge(1,2);B.add_edge(2,3);B.add_edge(2,4);B.add_edge(1,4);D=A.s_metric(B,normalized=False);C(D,19.0)
@B(A.NetworkXError)
def E():B=A.s_metric(A.Graph(),normalized=True)