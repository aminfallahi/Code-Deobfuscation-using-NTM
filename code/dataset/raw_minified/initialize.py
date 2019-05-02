from __future__ import absolute_import,print_function
def A():from numba.cuda.dispatcher import CUDADispatcher as A;return A
def B():from numba.targets.registry import dispatcher_registry as B;B.ondemand['gpu']=A;B.ondemand['cuda']=A