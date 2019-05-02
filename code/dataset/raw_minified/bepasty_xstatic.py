from xstatic.main import XStatic as C
A=['bootbox','bootstrap','jquery','jquery_ui','jquery_file_upload','pygments']
D=__import__('xstatic.pkg',fromlist=A)
E={}
for F in A:G=getattr(D,F);B=C(G,root_url='/static',provider='local',protocol='http');E[B.name]=B.base_dir