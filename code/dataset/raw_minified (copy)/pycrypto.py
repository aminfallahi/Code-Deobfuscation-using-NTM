from __future__ import absolute_import,unicode_literals
from Crypto.Cipher import AES
class A:
	def __init__(A,key):A.cipher=AES.new(key,AES.MODE_CBC,key[:16])
	def encrypt(A,plaintext):return A.cipher.encrypt(plaintext)
	def decrypt(A,ciphertext):return A.cipher.decrypt(ciphertext)