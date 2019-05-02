import json,andle.http,codecs as A
B='http://services.gradle.org/versions/current'
def C(url=B):
	try:B=A.getreader('utf-8');C=json.load(B(andle.http.request(url)));return C['version']
	except Exception:print('fail to connect url: '+url);return None