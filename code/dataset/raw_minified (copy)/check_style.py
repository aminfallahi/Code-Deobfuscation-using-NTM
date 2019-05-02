from os.path import join,dirname as A,abspath as B
import subprocess as C
D=A(B(__file__))
E=join(A(D),'src','SudsLibrary')
def F():A=['--max-line-length','150','.'];C.call(['pep8']+A,cwd=E)
if __name__=='__main__':F()