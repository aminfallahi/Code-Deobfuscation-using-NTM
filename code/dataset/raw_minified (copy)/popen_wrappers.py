B='/bin/echo / | xargs ls'
A=print
import commands as D,popen2 as C
A(D.getstatusoutput(B))
A(D.getoutput(B))
A(D.getstatus(B))
A(C.popen2(B)[0].read())
A(C.popen3(B)[0].read())
A(C.popen4(B)[0].read())
A(C.Popen3(B).fromchild.read())
A(C.Popen4(B).fromchild.read())