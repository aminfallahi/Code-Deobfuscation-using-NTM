from kafka.metrics.stats.sampled_stat import AbstractSampledStat as A
class B(A):
	'\n    An AbstractSampledStat that maintains a simple count of what it has seen.\n    '
	def __init__(A):super(B,A).__init__(0.0)
	def update(A,sample,config,value,now):sample.value+=1.0
	def combine(A,samples,config,now):return float(sum((A.value for A in samples)))