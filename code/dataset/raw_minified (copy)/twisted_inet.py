from twisted.application.service import ServiceMaker as A
B=A('Twisted INETD Server','twisted.runner.inetdtap','An inetd(8) replacement.','inetd')