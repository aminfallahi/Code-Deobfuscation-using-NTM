from zerotest.response import Response as A
def B():B=A(200,{'just test':'hope pass'},'happy test!');assert str(B)=="200\n{'just test': 'hope pass'}\nhappy test!"