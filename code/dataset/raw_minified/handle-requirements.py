I='requirements.txt'
H='-r'
G='install'
F=print
import sys,subprocess as A
if __name__=='__main__':
	B=[['pip',G,H,I],['/home/main/anaconda2/envs/python3/bin/pip',G,H,I]];C=0
	for D in B:
		try:F('Executing: {}'.format(D));sys.stdout.flush();A.check_call(D)
		except A.CalledProcessError as E:F('installation command failed: {}'.format(E));sys.stdout.flush();C+=1;continue
	if C>=len(B):raise Exception('All installation commands failed')