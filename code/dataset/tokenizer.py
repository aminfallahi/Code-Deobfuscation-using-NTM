import re
import os

def tokeniser( text, tokenpat=None, blockchar='()[]{}' ):
	'Lightweight text tokeniser for simple structured text'
	defpat = r'''
		(-?\d+\.?\d*)|  # find -nn.nnn or -nnn or nn numbers
		(\w+)|          # look for words (identifiers) next
		(".*?")|        # look for double-quoted strings
		('.*?')|        # look for single quoted strings
		([ \t]+)|       # gather white space (but not new lines)
		(\n)|           # check for a new line character
		(.)             # capture any other text as single characters'''
	openchar, closechar = blockchar[0::2], blockchar[1::2]
	blockpair = dict( zip( closechar, openchar ) )
	stack = []
	block = []
	synpat = re.compile( tokenpat or defpat, re.M + re.S + re.X )
	for token in synpat.split( text ):
		if token:
			if token in openchar:
				block.append( [] )
				stack.append( block )
				block = block[-1]
			block.append( token )
			if token in closechar:
				assert block[0] == blockpair[ token ], 'Block end mismatch'
				assert stack, 'Block start mismatch'
				block = stack.pop()
	assert stack == [], 'Block not closed'
	return block

def showtokens( tokens, indent=0 ):
	for token in tokens:
		if type( token ) == list:
			showtokens( token, indent+1 )
		else:
			print(token)

def getAllTokens():
	tokensFile=open("tokens","r")
	tokensStr=[]
	tokens=[]
	i=0
	for token in tokensFile:
		tokenActStr=bin(i)[2:].zfill(15)
		tokensStr.append(token.strip())
		tokenAct=[]
		for bit in tokenActStr:
			tokenAct.append(int(bit))
		tokens.append(tokenAct)
		i+=1
	return tokens,tokensStr


def printAllTokens(path):
	i=0
	for filename in os.listdir(path):
		i+=1
		print(filename,i)
		f=open(path+'/'+filename,'r')
		example=f.read()
		result = tokeniser( example )
		showtokens( result )
		f.close()

def flatten(lst):
	return sum( ([x] if not isinstance(x, list) else flatten(x) for x in lst), [] )

def generateActVect(content):
	tokens,tokensStr=getAllTokens()
	#print(tokens[tokensStr.index("import")])
	#exit()
	#f=open('./raw/'+filename,'r')
	#example=f.read()
	result = tokeniser( content )
	fileTokens=flatten(result)
	fileVectors=[]
	for fileToken in fileTokens:
		if fileToken in tokensStr:
			fileVectors.append(tokens[tokensStr.index(fileToken)])
	#print(fileVectors)
	#print(fileTokens)
	return fileVectors
#generateActVect('filter.py')
#printAllTokens('./raw')
#printAllTokens('./raw_minified')

for filename in os.listdir('./raw_minified'):
	fi=open('./raw/'+filename,'r')
	fo=open('./vectorized_raw_minified/'+filename,'w')
	vectors=generateActVect(fi.read())
	print(vectors,file=fo)
	fi.close()
	fo.close()
