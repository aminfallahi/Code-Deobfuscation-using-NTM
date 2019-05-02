import requests as A,lxml.html
def B():B=A.get('http://www.cdc.gov/zika/geo/active-countries.html');C=lxml.html.fromstring(B.content);D=C.cssselect('.list-block li');E=[A.text_content()for A in D];return E
if __name__=='__main__':print('\n'.join(B()))