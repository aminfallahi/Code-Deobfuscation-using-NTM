C=True
from kokki import Service as B,BooleanArgument as A
class D(B):provider='*monit.MonitServiceProvider';supports_restart=A(default=C);supports_status=A(default=C);supports_reload=A(default=False)