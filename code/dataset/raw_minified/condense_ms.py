F=set
def A(csv_data,environ):
	C='MS';A=csv_data;A.id_to_name[C]='Needs Microsoft Updates';A.id_to_severity[C]='High';D=F();E=F()
	for (B,G) in A.vuln_to_hosts.iteritems():
		if C in A.id_to_name[B][:2]or'Microsoft'in A.id_to_name[B]:
			D.add(B)
			for H in G:E.add(H)
	for I in D:del A.vuln_to_hosts[I]
	A.vuln_to_hosts[C]=E;A.rebuild_host_to_vulns()