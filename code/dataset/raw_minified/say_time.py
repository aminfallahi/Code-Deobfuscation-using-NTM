'Speak the time.'
__author__='T.V. Raman <raman@google.com>'
__copyright__='Copyright (c) 2009, Google Inc.'
__license__='Apache License, Version 2.0'
import android as A,time
B=A.Android()
B.ttsSpeak(time.strftime('%_I %M %p on %A, %B %_e, %Y '))