F=input
B='GuestList.txt'
C='w'
A=open(B,C)
for G in range(5):D=F('Enter guest name: ');E=F('Enter guest age: ');A.write(D+','+E+'\n')
A.close()