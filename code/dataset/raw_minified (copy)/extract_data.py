E=print
C=True
import sys,binwalk as D
for B in D.scan(*sys.argv[1:],signature=C,quiet=C,extract=C):
	E('%s Results:'%B.name)
	for A in B.results:
		if B.extractor.output.has_key(A.file.path):
			if B.extractor.output[A.file.path].extracted.has_key(A.offset):E("Extracted '%s' at offset 0x%X from '%s' to '%s'"%(A.description.split(',')[0],A.offset,A.file.path,str(B.extractor.output[A.file.path].extracted[A.offset])))