C='BTC'
B='1.063'
from sure import this as D
from decimal import Decimal as E
from coinbase.models import CoinbaseAmount as A
def F():D(A(B,C).amount).should.equal(E(B))
def G():D(A(B,C).currency).should.equal(C)
def H():D(A(E(B),C)).should.equal(A(B,C))