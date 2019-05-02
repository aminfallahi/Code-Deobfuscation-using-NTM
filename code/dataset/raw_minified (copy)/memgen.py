D='%02x\n'
E=128*1024
B=open('mem.hex','w')
for C in range(E):A=D%(C&255);B.write(A);A=D%(C>>8&255);B.write(A);A=D%(C>>16&255);B.write(A);A=D%(C>>24&255);B.write(A)