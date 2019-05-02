import DeepFried2 as A
class B(A.Criterion):
	def symb_forward(C,symb_input,symb_target):B=symb_target;A=symb_input;C._assert_same_dim(A,B);return abs(A-B)