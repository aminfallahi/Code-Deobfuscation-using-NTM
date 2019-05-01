wordsFile=open("words","r")
wordsStr=[]
words=[]
i=0
for word in wordsFile:
	wordActStr=bin(i)[2:].zfill(8)
	wordsStr.append(word.strip())
	wordAct=[]
	for bit in wordActStr:
		wordAct.append(int(bit))
	words.append(wordAct)
	i+=1
#print(words)
#print(wordsStr)

f=open("3.mini.py","r")
fileWords=[]
fileWordsStr=[]
for line in f:
	_fileWords=line.split()
	for _fileWord in _fileWords:
		fileWords.append(words[wordsStr.index(_fileWord)])
		fileWordsStr.append(_fileWord)
print(fileWords)
#print(fileWordsStr)
