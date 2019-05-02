from run_notebook import run
def A():
	C=run('../notebooks/wide_area_plots.ipynb')
	for (A,B) in C['figures'].items():
		if A not in['l317','l305','l299']:continue
		B.set_tight_layout(True);B.savefig(A+'.eps')
if __name__=='__main__':A()