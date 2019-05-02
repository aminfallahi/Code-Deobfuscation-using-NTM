from flask import Blueprint as C,render_template as D,jsonify as E,redirect as F,url_for as G
from flask_website.utils import request_wants_json as H
from flask_website.listings.extensions import extensions as A,unlisted as I
B=C('extensions',__name__,url_prefix='/extensions')
@B.route('/')
def J():
	if H():return E(extensions=[B.to_json()for B in A],unlisted_extensions=[A.to_json()for A in I])
	return D('extensions/index.html',extensions=A)
@B.route('/creating/')
def K():return F(G('docs.show',page='extensiondev'),301)