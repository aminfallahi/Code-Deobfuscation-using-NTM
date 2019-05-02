from twisted.application.service import ServiceMaker as A
B=A('Twisted Conch Server','twisted.conch.tap','A Conch SSH service.','conch')
C=A('Twisted Manhole (new)','twisted.conch.manhole_tap','An interactive remote debugger service accessible via telnet and ssh and providing syntax coloring and basic line editing functionality.','manhole')