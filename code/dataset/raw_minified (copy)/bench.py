E='prof'
import sys
if __name__=='__main__':import cProfile as B,pytest,pstats as C;D=sys.argv[1:]if len(sys.argv)>1 else'empty.py';F=B.run('pytest.cmdline.main(%r)'%D,E);A=C.Stats(E);A.strip_dirs();A.sort_stats('cumulative');print(A.print_stats(500))