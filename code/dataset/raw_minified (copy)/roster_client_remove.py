import sys
from twisted.internet import reactor as A
from twisted.words.protocols.jabber.jid import JID
from wokkel.client import XMPPClient as D
from wokkel.xmppim import RosterClientProtocol as E
F,G,H=sys.argv[1:4]
B=D(JID(F),G)
C=E()
C.setHandlerParent(B)
I=C.removeItem(JID(H))
I.addBoth(lambda _:A.stop())
B.startService()
A.run()