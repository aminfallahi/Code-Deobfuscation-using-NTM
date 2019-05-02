'One user repeatedly logs in, logs out.  Allow interleaving with other actions'
C='VinniPuhh'
from WebModel import Login as A,Logout as B
D=A,B
E=0
F=0,
G=(0,(A,(C,'Correct'),'Success'),1),(1,(B,(C,),None),0)