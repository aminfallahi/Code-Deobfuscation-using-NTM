D=min
A=float
import sys
from kafka.metrics.stats.sampled_stat import AbstractSampledStat as B
class C(B):
	'An AbstractSampledStat that gives the min over its samples.'
	def __init__(B):super(C,B).__init__(A(sys.maxsize))
	def update(B,sample,config,value,now):A=sample;A.value=D(A.value,value)
	def combine(C,samples,config,now):
		B=samples
		if not B:return A(sys.maxsize)
		return A(D((A.value for A in B)))