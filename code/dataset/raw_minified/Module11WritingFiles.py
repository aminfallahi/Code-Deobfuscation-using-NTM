B='demo.txt'
C='w'
E='a'
D=input('Please enter file info')
A=open(B,mode=C)
A.write(D)
A.close()
print('File written successfully')