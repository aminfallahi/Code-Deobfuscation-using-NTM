import logging as A,requests as B
C=A.getLogger(__name__)
def D(url,verify=True):
	'\n    Retrieves HTML from the provided URL.\n    ';C.debug('Requesting %s'%url);A=B.get(url);D=A.text
	if verify and'html'not in A.headers['content-type']:raise ValueError('Response does not have an HTML content-type')
	return D