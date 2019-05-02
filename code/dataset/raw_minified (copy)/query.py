from hotqueue import key_for_name as B
def A(store,*C):
	'Return a generator that yields the queue name and number of items for\n    each of the given queue names in the given Redis class instance.\n    '
	for A in C:(yield(A,store.llen(B(A))))