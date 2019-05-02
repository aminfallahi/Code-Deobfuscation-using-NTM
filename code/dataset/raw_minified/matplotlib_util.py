'\nCreated on Mar 29, 2010\n\n@author: Zachary Varberg\n'
D=sum
from matplotlib import pyplot as A
def B(my_list,ave_length):C=ave_length;B=my_list;A.plot([D(B[A-C:A])/C if A>=C else D(B[0:A])/A for A in xrange(1,len(B))])