E=print
from scipy.cluster.hierarchy import linkage as A
from scipy.spatial.distance import pdist
from sklearn.datasets import make_blobs as B
E('I: Simulating 4 blobs')
C,F=B(centers=4)
D=pdist(C,metric='euclidean')
G=A(D,method='single')
E('I: Done clustering 4 blobs')