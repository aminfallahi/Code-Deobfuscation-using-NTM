import imp,json,os as A,sys
D=A.path.dirname(__file__)
E=imp.load_source('localpaths',A.path.abspath(A.path.join(D,A.pardir,'localpaths.py')))
B=E.repo_root
import manifest as C
def F(request,response):D=A.path.join(B,'MANIFEST.json');E=C.manifest.load(B,D);C.update.update(B,'/',E);C.manifest.write(E,D);return[('Content-Type','application/json')],json.dumps({'url':'/MANIFEST.json'})