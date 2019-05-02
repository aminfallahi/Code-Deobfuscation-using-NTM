'\nUtilities for handling the cmap table\nand character mapping in general.\n'
def A(ttFont):return ttFont['cmap'].getcmap(3,1).cmap
def B(cmap):
	reversed={}
	for (B,A) in cmap.items():
		if A not in reversed:reversed[A]=[]
		reversed[A].append(B)
	return reversed