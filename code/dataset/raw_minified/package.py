import zipfile as A,qisys.qixml
from qisys.qixml import etree
def B(archive_path):B=A.ZipFile(archive_path);C=B.read('manifest.xml');D=etree.fromstring(C);return D.get('uuid')