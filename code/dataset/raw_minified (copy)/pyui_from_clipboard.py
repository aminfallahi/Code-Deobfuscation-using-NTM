import clipboard as A
B='pyui_from_clipboard.pyui'
assert A.get(),'There is no text on the clipboard!'
with open(B,'w')as C:C.write(A.get())
print('The contents of the clipboard are now on file {}.'.format(B))