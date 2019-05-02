import numpy as np
import os
from pprint import pprint
import random

np.set_printoptions(threshold=np.inf)

def _generate_data(num_batches,batch_size):
	for nb in range(num_batches):
		batchesInput=[]
		batchesOutput=[]
		m=0
		files=os.listdir('./vectorized_raw_minified')
		random.shuffle(files)
		files=files[0:batch_size]
		#input
		for filename in files:
			f=open('./vectorized_raw_minified/'+filename,"r")
			inp=eval(f.read())
			if len(inp)>m:
				m=len(inp)

			for i in range(len(inp)):
				inp[i].append(0)
			for i in range(128-len(inp)):
				inp.append([0]*len(inp[0]))
			inp.append([1]*len(inp[0]))
			for i in range(128):
				inp.append([0]*len(inp[0]))
			batchesInput.append(inp)
			f.close()
		#output

		m=0
		for filename in files:
			f=open('./vectorized_raw/'+filename,"r")
			inp=eval(f.read())
			if len(inp)>m:
				m=len(inp)
			for i in range(128-len(inp)):
				inp.append([0]*len(inp[0]))
			batchesOutput.append(inp)
			f.close()

		batches=[]
		batches.append((128,np.asarray(batchesInput),np.asarray(batchesOutput)))
		#pprint(batches[0][1])
	return batches
