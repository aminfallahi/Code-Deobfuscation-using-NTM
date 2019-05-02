import re
def A(csv_data,regex,options):
	B=csv_data;C=set()
	for A in B.host_to_vulns.keys():
		if re.search(regex,A)==None:C.add(A)
	for A in C:del B.host_to_vulns[A]
	B.rebuild_vuln_to_hosts()