class A:
	def test_get_latest(B,client):A=client.get('/latest');assert 200==A.status_code;assert'text/html'==A.mimetype;assert'<img src="/latest.jpg"'in A.get_data(as_text=True)