from MySQLdb import connect as B
import numpy as C,cPickle as D
E='catalog.pkl'
F=B(host='localhost',user='beaumont',db='mwp')
A=F.cursor()
A.execute('select lon, lat, angle, semi_major, semi_minor, thickness, hit_rate from clean_bubbles_anna')
G=C.array([map(float,B)for B in A.fetchall()])
with open(E,'w')as H:D.dump(G,H)