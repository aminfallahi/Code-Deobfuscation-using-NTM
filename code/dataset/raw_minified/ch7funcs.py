def A(datasource,layer_name,field_name):
	B=field_name;A=datasource;E='SELECT DISTINCT {0} FROM {1}'.format(B,layer_name);C=A.ExecuteSQL(E);D=[]
	for F in C:D.append(F.GetField(B))
	A.ReleaseResultSet(C);return D