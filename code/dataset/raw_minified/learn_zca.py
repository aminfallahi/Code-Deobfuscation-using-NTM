from pylearn2.datasets.preprocessing import ZCA
from pylearn2.utils import serial as B
from black_box_dataset import BlackBoxDataset as C
D=C('extra')
A=ZCA(filter_bias=0.1)
A.fit(D.X)
B.save('zca.pkl',A)