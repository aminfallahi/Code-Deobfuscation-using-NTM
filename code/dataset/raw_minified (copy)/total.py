from kafka.metrics.measurable_stat import AbstractMeasurableStat as A
class B(A):
	'An un-windowed cumulative total maintained over all time.'
	def __init__(A,value=0.0):A._total=value
	def record(A,config,value,now):A._total+=value
	def measure(A,config,now):return float(A._total)