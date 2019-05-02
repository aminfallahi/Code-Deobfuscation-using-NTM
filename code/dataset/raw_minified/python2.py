'wrapper for python2, required by emscripten'
C=True
B='python2'
import subprocess as A
D=B
E=['osx','linux']
F=C
G="required for emscripten, on OSX run 'brew install python'"
def H(fips_dir):
	try:A.check_output([B,'--version'],stderr=A.STDOUT);return C
	except (OSError,A.CalledProcessError):return False