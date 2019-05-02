'This script will call HLR lookup api to get the MCC/MNC of the destination number'
B='mcc'
import requests as C,json
D='https://api.some-provider.com/hlr/lookup'
E=json.dumps({'number':routable.pdu.params['destination_addr']})
A=C.post(D,E,auth=('user','*****'))
if A.json['mnc']=='214':
	if A.json[B]=='01':routable.addTag(21401)
	elif A.json[B]=='03':routable.addTag(21403)
	elif A.json[B]=='25':routable.addTag(21425)