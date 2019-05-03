import numpy as np
import os
from pprint import pprint
import random

np.set_printoptions(threshold=np.inf)

def _generate_data(num_batches,batch_size,num_bits,seq_len):
	batches=[]
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

			#shorten number of bits per vector
			for i in range(len(inp)):
				inp[i]=inp[i][0:num_bits]
			
			for i in range(len(inp)):
				inp[i].append(0)
			
			#fix sequence length
			if len(inp)<seq_len:
				for i in range(seq_len-len(inp)):
					inp.append([0]*len(inp[0]))
			inp=inp[0:seq_len]
			
			inp.append([1]*len(inp[0]))

			for i in range(seq_len):
				inp.append([0]*len(inp[0]))
			print(inp)
			exit()
			batchesInput.append(inp)
			f.close()
		#output
		m=0
		for filename in files:
			f=open('./vectorized_raw/'+filename,"r")
			inp=eval(f.read())
			if len(inp)>m:
				m=len(inp)

			#shorten number of bits per vector
			for i in range(len(inp)):
				inp[i]=inp[i][0:num_bits]

			#fix sequence length
			if len(inp)<seq_len:
				for i in range(seq_len-len(inp)):
					inp.append([0]*len(inp[0]))
			inp=inp[0:seq_len]

			batchesOutput.append(inp)
			f.close()
		
		batches.append((seq_len,np.float32(np.asarray(batchesInput)),np.float32(np.asarray(batchesOutput))))
	np.set_printoptions(threshold=np.inf)
	#pprint(batches)
	return batches
_generate_data(3,5,8,20)
