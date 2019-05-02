'Test that foreign keys with non-trivial keys are properly ignored.'
B=False
from sandman.model import activate as A
A(admin=B,browser=B,reflect_all=True)