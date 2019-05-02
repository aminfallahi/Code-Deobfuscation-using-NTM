from __future__ import absolute_import,unicode_literals
D='ohai'
C='f.txt'
from pre_commit_hooks import check_byte_order_marker as A
def B(tmpdir):B=tmpdir.join(C);B.write_text(D,encoding='utf-8-sig');assert A.main((B.strpath,))==1
def E(tmpdir):B=tmpdir.join(C);B.write_text(D,encoding='utf-8');assert A.main((B.strpath,))==0