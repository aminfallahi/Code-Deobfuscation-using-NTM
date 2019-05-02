A=CoramIoRegister(idx=0,datawidth=32,size=32)
B=CoramRegister(idx=0,datawidth=32)
while True:C=B.read();A.write(0,C)