import os,sys
from pylearn2.utils import serial as A
from sklearn.externals.joblib import dump
if os.path.exists('../../galatea'):sys.path.append('../../')
B=A.load(sys.argv[1])
C=B.generator.mlp
dump(C.get_param_values(),'generator_params.jb')