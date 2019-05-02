class A:
	'\n    Language is to store the detected language.\n    Detector.get_probabilities() returns a list of Languages.\n    '
	def __init__(A,lang,prob):A.lang=lang;A.prob=prob
	def __repr__(A):
		if A.lang is None:return''
		return'%s:%s'%(A.lang,A.prob)
	def __lt__(A,other):return A.prob<other.prob