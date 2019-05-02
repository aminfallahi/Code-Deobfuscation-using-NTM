from expecter import expect as A
def B():
	def B(client):B=client.get('/');A(B.status_code)==200;A(B.mimetype)=='text/html';A(B.get_data(as_text=True)).contains('meme generator')