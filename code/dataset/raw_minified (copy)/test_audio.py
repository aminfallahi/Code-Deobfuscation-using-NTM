C=bytearray
from captcha.audio import AudioCaptcha as A
def B():D=A();B=D.generate('1234');assert isinstance(B,C);assert C(b'RIFF')in B
def D():B=A();C=B.random(4);assert len(C)==4