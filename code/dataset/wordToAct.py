def getAllWords():
	wordsFile=open("tokens","r")
	wordsStr=[]
	words=[]
	i=0
	for word in wordsFile:
		wordActStr=bin(i)[2:].zfill(15)
		wordsStr.append(word.strip())
		wordAct=[]
		for bit in wordActStr:
			wordAct.append(int(bit))
		words.append(wordAct)
		i+=1
	return words,wordsStr

words,wordsStr=getAllWords()
print(words[wordsStr.index("import")])
exit()


f=open("./raw/filter.py","r")
fileWords=[]
fileWordsStr=[]
for line in f:
	_fileWords=line.split()
	for _fileWord in _fileWords:
		fileWords.append(words[wordsStr.index(_fileWord)])
		fileWordsStr.append(_fileWord)
print(fileWords)
#print(fileWordsStr)
