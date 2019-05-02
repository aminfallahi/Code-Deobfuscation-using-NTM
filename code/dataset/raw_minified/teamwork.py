def A(api,data):
	E=True;D=False;B=api.team.get_team_members(tid=data['tid'])
	if len(B)<2:A=D
	else:
		A=E
		for C in B:
			if api.problem.count_submissions(uid=C['uid'],correctness=E)<1:A=D;break
	return A,{}