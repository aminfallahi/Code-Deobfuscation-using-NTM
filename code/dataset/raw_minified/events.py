from flask import request as A
from redash.handlers.base import BaseResource as B
class C(B):
	def post(B):
		C=A.get_json(force=True)
		for D in C:B.record_event(D)