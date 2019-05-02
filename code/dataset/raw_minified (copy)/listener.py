from circus.consumer import CircusConsumer as A
import json
B='tcp://127.0.0.1:5556'
C='show:'
for (D,E) in A(C,endpoint=B):F=json.dumps(dict(message=D,topic=E));print(F)