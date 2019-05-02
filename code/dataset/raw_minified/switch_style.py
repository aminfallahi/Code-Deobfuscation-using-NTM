import re
def A(junos,facts):
	E='NONE';B=facts;C=B['personality']
	if C in['MX','SRX_HIGHEND']:A='BRIDGE_DOMAIN'
	elif C in['SWITCH','SRX_BRANCH']:
		D=B['model']
		if re.match('firefly',D,re.IGNORECASE):A=E
		elif re.match('^(EX9)|(EX43)',D):A='VLAN_L2NG'
		else:A='VLAN'
	else:A=E
	B['switch_style']=A