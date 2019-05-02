A=property
class B:
	def __init__(A,metric_name,percentile):A._metric_name=metric_name;A._percentile=float(percentile)
	@A
	def name(self):return self._metric_name
	@A
	def percentile(self):return self._percentile