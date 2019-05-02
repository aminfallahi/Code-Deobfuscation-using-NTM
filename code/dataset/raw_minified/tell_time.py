from datetime import datetime as A
from SenseCells.tts import tts
def B():tts('The time is '+A.strftime(A.now(),'%H:%M:%S'))