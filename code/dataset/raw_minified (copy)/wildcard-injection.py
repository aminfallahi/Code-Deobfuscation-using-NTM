F='tar'
E='/bin/chmod *'
D='/bin/chown *'
C='*'
import os as B,subprocess as A
B.system('/bin/tar xvzf *')
B.system(D)
B.popen2(E)
A.Popen(D,shell=True)
A.Popen('/bin/rsync *')
A.Popen(E)
A.Popen(['/bin/chown',C])
A.Popen(['/bin/chmod',sys.argv[1],C],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
B.spawnvp(os.P_WAIT,F,[F,'xvzf',C])