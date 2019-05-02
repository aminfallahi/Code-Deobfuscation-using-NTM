import angr as D,logging as A
F=A.getLogger('angr.tests')
import os as B
E=str(B.path.join(B.path.dirname(B.path.realpath(__file__)),'../../binaries/tests'))
def C():G='fauxware';F='x86_64';A=D.Project(B.path.join(E,F,G),translation_cache=True);C=A.factory.block(A.entry);assert A.factory.block(A.entry)is C;A=D.Project(B.path.join(E,F,G),translation_cache=False);C=A.factory.block(A.entry);assert A.factory.block(A.entry)is not C
if __name__=='__main__':C()