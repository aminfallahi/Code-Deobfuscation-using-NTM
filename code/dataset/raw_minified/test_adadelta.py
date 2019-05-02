from neupy import algorithms as B
from data import simple_classification as C
from base import BaseTestCase as A
class D(A):
	def test_simple_adadelta(D):E,F,G,F=C();A=B.Adadelta((10,20,1),step=2.0,batch_size='full',verbose=False,decay=0.95,epsilon=1e-05);A.train(E,G,epochs=100);D.assertAlmostEqual(0.04,A.errors.last(),places=2)