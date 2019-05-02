B,C=preprocess(data,shuffle=False,n_samples=1000,normalization=None)
from sklearn.manifold import LocallyLinearEmbedding as D
E=D(n_neighbors=15,n_components=3,method='modified')
A=E.fit_transform(B)
three_component_plot(A[:,0],A[:,1],A[:,2],C,labels,trim_outliers=True)