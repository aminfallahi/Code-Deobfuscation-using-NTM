C=TypeError
B=len
class A:
	def action_given_state(D,state):
		A=state
		if B(A)!=1:raise C('expect only single value in state, not %d values'%B(A))
		A=A[0]
		if A not in[0,1,2]:raise C('expect only 0,1,2 not %d'%A)
		return A
	def train(A,state_1,action,reward,state_2):0