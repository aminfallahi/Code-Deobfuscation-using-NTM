F='..'
import os.path as A
from nose.tools import assert_true as C
from mne.io import Raw
from mne.preprocessing.eog import find_eog_events as D
B=A.join(A.dirname(__file__),F,F,'io','tests','data')
E=A.join(B,'test_raw.fif')
G=A.join(B,'test-eve.fif')
H=A.join(B,'test-proj.fif')
def I():'Test find EOG peaks';A=Raw(E);B=D(A);F=len(B);C(F==4)