import pip
A=['unidecode','wikipedia','whoosh','nltk','scikit-learn','regex','fuzzywuzzy','python-Levenshtein','kenlm','pattern']
def B(package):pip.main(['install',package])
if __name__=='__main__':
	for C in A:B(C)