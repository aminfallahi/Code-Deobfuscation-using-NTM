'These routines assume 1D ODEs\n'
from numpy import linspace as D,zeros
def E(DS,t,x,dt):'Use for PyDSTool generators given by DS argument\n    ';return x+dt*DS.Rhs(t,{DS.variables.keys()[0]:x})[0]
def A(DS,t0,t1,dt,x0):
	A=D(t0,t1,(t1-t0)/dt);C=zeros(len(A),float);B=x0
	for (F,G) in enumerate(A):C[F]=B;B=E(DS,G,B,dt)
	return A,C