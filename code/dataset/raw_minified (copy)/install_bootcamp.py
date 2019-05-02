import subprocess as A,os
B=['"BootCampAutoUnattend" IN tags']
for C in B:A.call(['/usr/bin/python',os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'predicate_installer.py'),C])