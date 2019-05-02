from twisted.application.service import ServiceMaker as A
B=A('Twisted Telnet Shell Server','twisted.tap.telnet','A simple, telnet-based remote debugging service.','telnet')