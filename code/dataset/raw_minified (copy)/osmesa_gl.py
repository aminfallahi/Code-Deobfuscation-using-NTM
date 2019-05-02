import os
from .  import logger as A
def B():
	'\n    When using OSMesa, the gl functions (from libGL) are included\n    in libOSMesa.so. This function modifies the VISPY_GL_LIB env variable\n    so gl2 picks up libOSMesa.so as the OpenGL library.\n\n    This modification must be done before vispy.gloo is imported for the\n    first time.\n    ';B='VISPY_GL_LIB'
	if B in os.environ:A.warning('VISPY_GL_LIB is ignored when using OSMesa. Use OSMESA_LIBRARY instead.')
	os.environ[B]=os.getenv('OSMESA_LIBRARY','libOSMesa.so')