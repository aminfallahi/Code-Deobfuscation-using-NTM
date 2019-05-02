import clipboard as B
A='put_your_filename_here.pyui'
with open(A)as C:B.set(C.read())
print('The contents of {} are now on the clipboard.'.format(A))