'Converts a timed-0.11-style log file to a timed-0.12-style log file.'
import timed as A,yaml
def B():
	B=open(A.log_file).read()
	if not B:return[]
	return yaml.safe_load(B)
C=B()
A.save(C)