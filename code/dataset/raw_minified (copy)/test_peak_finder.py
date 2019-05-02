from numpy.testing import assert_array_equal as A
from mne.preprocessing.peak_finder import peak_finder as B
def C():'Test the peak detection method';C=[0,2,5,0,6,-1];D,E=B(C);A(D,[2,4])