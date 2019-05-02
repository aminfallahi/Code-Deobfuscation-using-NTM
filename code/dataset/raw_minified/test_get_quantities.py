import numpy as D
from ..  import Model
from ...util.functions import random_id as B
from .test_helpers import get_test_dust as E
def A(tmpdir):C=tmpdir;A=Model();A.set_cartesian_grid([-1.0,1.0],[-1.0,1.0],[-1.0,1.0]);A.add_density_grid(D.array([[[1.0]]]),E());A.set_n_initial_iterations(0);A.set_n_photons(imaging=1);A.write(C.join(B()).strpath);F=A.run(C.join(B()).strpath);G=F.get_quantities();assert'density'in G