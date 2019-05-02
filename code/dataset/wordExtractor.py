import os

for filename in os.listdir('./raw'):
	f=open('./raw/'+filename,"r")
	words=[]
	for line in f:
		_words=line.split()
		for word in _words:
			words.append(word)
	print(words)
