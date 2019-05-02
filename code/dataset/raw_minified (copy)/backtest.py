import six
class A:
	'Base class for a Tradewave backtest'
	def __init__(A,strategy_id,id=None,**B):
		A.id=id;A.strategy_id=strategy_id
		for (C,D) in six.iteritems(B):setattr(A,C,D)