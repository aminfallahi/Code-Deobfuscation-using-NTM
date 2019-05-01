f=open("1.py","r")
words=[]
for line in f:
	_words=line.split()
	for word in _words:
		words.append(word)
print(words)
