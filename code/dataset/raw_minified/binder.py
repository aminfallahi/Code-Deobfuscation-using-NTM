from importlib import import_module as A
from flows import config as B
def D(request):return request.session.session_key
def C():C=B.FLOWS_TASK_BINDER;D,E=C.rsplit('.',1);F=A(D);return getattr(F,E)
E=C()