from pbkdf2 import crypt as A
def B(secret):return A(secret)
def C(secret,pwhash):B=pwhash;return B==A(secret,B)