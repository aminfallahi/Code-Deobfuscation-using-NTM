import re
def A(line):
	"Returns an indent at head of the specified line.\n\n    Usage::\n        >>> line_indent('    I have 4 spaces.')\n        '    '\n    ";A='';B=re.search('^(\\s*)',line)
	if len(B.groups())>=1:A=B.group(1)
	return A