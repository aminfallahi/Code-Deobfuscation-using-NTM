B=None
A=type
import pytest as C
from autobahn.websocket.compress import PerMessageDeflateOffer as D,PerMessageDeflateOfferAccept as E
from aiorest_ws.utils.websocket import deflate_offer_accept as F
@C.mark.parametrize('offers, expected',[([D()],E),([B],A(B)),([],A(B))])
def G(offers,expected):assert A(F(offers))is expected