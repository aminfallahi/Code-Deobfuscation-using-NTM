'\nShow use of colorbars in plot\n'
import vispy.plot as C
A=C.Fig(size=(600,500),show=False)
B=A[(0,0)]
A.title='bollu'
B.plot([(A,A**2)for A in range(0,100)],title='y = x^2')
B.colorbar(position='top',cmap='autumn')
if __name__=='__main__':A.show(run=True)