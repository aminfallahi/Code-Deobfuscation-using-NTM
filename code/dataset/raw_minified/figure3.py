from load_ml100k import load
from matplotlib import pyplot as A
B=load()
A.gray()
A.imshow(B[:200,:200],interpolation='nearest')
A.xlabel('User ID')
A.ylabel('Film ID')
A.savefig('Figure_08_03_DataMatrix.png')