import tables as A,numpy as B
class C(A.IsDescription):timestamp=A.Time64Col();symbol=A.StringCol(30);shares=A.Int32Col();purchase_price=A.Float32Col()