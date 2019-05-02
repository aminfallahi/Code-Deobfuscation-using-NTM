'Original NetworkX graph tests'
from nose.tools import *
import networkx,networkx as nx
from historical_tests import HistoricalTests
class TestGraphHistorical(HistoricalTests):
	def setUp(self):HistoricalTests.setUp(self);self.G=nx.Graph