def A(api,data):
	A=api;E=A.stats.get_pid_categories();F=A.problem.get_solved_pids(tid=data['tid']);B=set()
	for G in F:B.add(E[G])
	C=True
	for D in A.problem.get_all_categories():
		if D not in B:
			if D!='Master Challenge':C=False;break
	return C,{}