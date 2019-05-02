E=print
import clang.cindex,sys as A,os.path
if len(A.argv)!=3:E('Usage: complete.py [libclang.(so|dylib)] [cpp file]');A.exit()
clang.cindex.Config.set_library_file(A.argv[1])
B=clang.cindex.Index.create()
C=B.parse(os.path.abspath(A.argv[2]),['-x','c++','-std=c++11'])
D=C.codeComplete(A.argv[2],6,11)
E(list(D.results))