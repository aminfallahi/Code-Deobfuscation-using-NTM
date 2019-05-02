import random as E,numpy,model as A
B=A.get_data()
F=B.shape[0]
C=numpy.zeros((62,64,64))
for D in xrange(62):C[D]=E.choice(B)[D]*1.0/255
A.draw_grid(C).save('alphabet.png')