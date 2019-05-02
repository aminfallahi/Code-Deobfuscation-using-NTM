from django.db.backends import BaseDatabaseClient as B
from django.conf import settings as A
import os
class C(B):
	executable_name='psql'
	def runshell(C):
		B=[C.executable_name]
		if A.DATABASE_USER:B+=['-U',A.DATABASE_USER]
		if A.DATABASE_PASSWORD:B+=['-W']
		if A.DATABASE_HOST:B.extend(['-h',A.DATABASE_HOST])
		if A.DATABASE_PORT:B.extend(['-p',str(A.DATABASE_PORT)])
		B+=[A.DATABASE_NAME];os.execvp(C.executable_name,B)