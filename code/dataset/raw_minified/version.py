"\nProvides gitver's version by dynamically loading the optional _version module.\n"
B=None
C=B
D=B
E=B
try:import _version as A;C=A.gitver_version;D=A.gitver_buildid;E=A.gitver_pypi
except ImportError:pass