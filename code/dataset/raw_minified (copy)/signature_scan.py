E=True
D=print
import sys,binwalk as B
try:
	for C in B.scan(*sys.argv[1:],signature=E,quiet=E):
		D('%s Results:'%C.name)
		for A in C.results:D('\t%s    0x%.8X    %s [%s]'%(A.file.name,A.offset,A.description,str(A.valid)))
except B.ModuleException as F:pass