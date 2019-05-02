import subprocess as B,os as A
C=['"com.apple.java.runtime" IN tags']
A.environ['JAVA_INSTALL_ON_DEMAND']='1'
for D in C:B.call(['/usr/bin/python',A.path.join(A.path.dirname(A.path.dirname(A.path.abspath(__file__))),'predicate_installer.py'),D])