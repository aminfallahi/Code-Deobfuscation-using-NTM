'\nCreated on Feb 22, 2013\n\n@organization: cert.org\n'
from .  import BanditArmBase as A
class B(A):
	"\n    This class implements a Bayesian estimator on a Bernoulli process where\n    each pull of the arm results in either a success with probability p.\n\n    Uses Laplace's Law of Succession\n    "
	def _update_p(A,successes=0,trials=0):A.probability=(A.successes+1.0)/(A.trials+2.0)