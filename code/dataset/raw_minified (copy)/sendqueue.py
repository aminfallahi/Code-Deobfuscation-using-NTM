class A:
	'\n    Queues packets to send when transport can send\n    '
	def __init__(A,transport,can_send_func=lambda:True,pre_process_func=lambda x:x):A._q=[];A._transport=transport;A._can_send=can_send_func;A._pre_process=pre_process_func
	def send(A,packet=None):
		C=packet
		if C:A._q.append(C)
		if A._can_send():
			for B in A._q:B=A._pre_process(B);A._transport.write(B)
			A._q.clear()