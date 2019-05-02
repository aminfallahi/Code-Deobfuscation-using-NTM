import re
class A:
	def validate(A,value):return bool(re.match(A.regex,value))
def B(name,regex):return type(name,(A,),{'regex':regex})