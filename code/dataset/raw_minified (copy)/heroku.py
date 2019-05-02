import requests as C,netrc,valor as B
A=C.Session()
A.auth='',netrc.netrc().hosts['api.heroku.com'][2]
A.headers['Accept']='application/vnd.heroku+json; version=3'
D=B.Schema.from_file('tests/schema.json')
E=B.Service(schema=D,session=A)