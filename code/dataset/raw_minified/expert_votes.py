from run_notebook import run
def A():
	B=run('../notebooks/Expert_Votes.ipynb')
	for (C,A) in B['figures'].items():A.set_tight_layout(True);A.savefig('expert_'+C+'.eps')
if __name__=='__main__':A()