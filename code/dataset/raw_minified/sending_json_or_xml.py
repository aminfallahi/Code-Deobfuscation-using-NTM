_C='bar'
_B='moof'
_A='foo'
import json,xml.etree.ElementTree as etree
from itty import *
@get('/json')
def send_json(request):return Response(json.dumps({_A:_C,_B:123}),content_type='application/json')
@get('/xml')
def send_xml(request):xml=etree.Element('doc');foo=etree.SubElement(xml,_A,value=_C);foo=etree.SubElement(xml,_B,value='123');return Response(etree.tostring(xml),content_type='application/xml')
run_itty()