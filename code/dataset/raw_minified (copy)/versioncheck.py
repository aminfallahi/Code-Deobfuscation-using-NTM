"\nCopyright (c) 2014-2016 Miroslav Stampar (@stamparm)\nSee the file 'LICENSE' for copying permission\n"
import sys
A=sys.version.split()[0]
if A>='3'or A<'2.6':exit("[CRITICAL] incompatible Python version detected ('%s'). For successfully running Maltrail you'll have to use version 2.6 or 2.7 (visit 'http://www.python.org/download/')"%A)