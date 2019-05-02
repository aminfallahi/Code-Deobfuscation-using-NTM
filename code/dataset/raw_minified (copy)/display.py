B=round
class A:
	"\n        Round Glucose values for display, so that they are consistent in\n        all OpenAPS apps\n\n        Example:\n\n            from openaps.glucose.display import Display\n            print(Display.display('mmol/L', 5.5))\n            print(Display.display('mg/dL', 100))\n    "
	@classmethod
	def display(E,unit,val):
		D='mg/dL';C='mmol/L';A=unit;assert A in[C,D]
		if A==D:return int(B(val))
		elif A==C:return B(val,1)