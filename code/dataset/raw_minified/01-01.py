E='diag'
A=gmm.GMM(1,E)
B=y_train==0
A.fit(X_train[B])
C=gmm.GMM(1,E)
D=y_train==1
C.fit(X_train[D])