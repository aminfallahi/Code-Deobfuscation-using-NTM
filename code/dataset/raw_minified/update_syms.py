__author__='c01db33f@gmail.com'
def A(vdb,line):'\n    update the vdb currently loaded libraries\n    ';A=vdb.getTrace();A._findLibraryMaps('\x7fELF')
def B(vdb,trace):vdb.registerCmdExtension(A)