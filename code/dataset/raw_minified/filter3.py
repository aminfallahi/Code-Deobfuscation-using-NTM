'\nPyModel configuration - state filter, limit population to 3\n'
import populations as A
def B():return len(A.population)<=3
A.StateFilter=B