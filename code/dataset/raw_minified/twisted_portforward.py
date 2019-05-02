from twisted.application.service import ServiceMaker as A
B=A('Twisted Port-Forwarding','twisted.tap.portforward','A simple port-forwarder.','portforward')