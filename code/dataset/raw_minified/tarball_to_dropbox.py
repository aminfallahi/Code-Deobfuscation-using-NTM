import dropboxlogin as B,os,tarfile as C
A='my_archive.tar'
with C.open(A,'w')as D:D.add(os.path.basename(__file__))
with open(A)as E:B.get_client().put_file(A,E,overwrite=True)