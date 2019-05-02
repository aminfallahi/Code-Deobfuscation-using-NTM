from run_notebook import run
def A():
	C=run('../notebooks/full_search_distributions.ipynb')
	for (A,B) in C['figures'].items():
		if A=='new_gallery':B.savefig(A+'.eps')
		if A=='score':B.savefig('new_score.eps')
if __name__=='__main__':A()