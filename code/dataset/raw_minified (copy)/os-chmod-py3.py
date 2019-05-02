B='/etc/passwd'
import os as A,stat
C='foo'
A.chmod(B,151)
A.chmod(B,7)
A.chmod(B,436)
A.chmod(B,511)
A.chmod(B,504)
A.chmod(B,510)
A.chmod(B,496)
A.chmod('~/.bashrc',511)
A.chmod('/etc/hosts',511)
A.chmod('/tmp/oh_hai',511)
A.chmod(B,stat.S_IRWXU)
A.chmod(key_file,511)