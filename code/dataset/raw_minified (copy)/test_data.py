from bepasty.storage.filesystem import Data
def A(tmpdir):B=b'a';C=tmpdir.join('test.data');A=Data(C.open('w+b'));assert A.size==0;A.write(B*1024,0);assert A.size==1024;A.write(B*1024,1024*3);assert A.size==1024*4;assert A.read(1024,0)==B*1024;assert A.read(1024,1024)==b'\x00'*1024;A.close()