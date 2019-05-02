C='..'
import os as A,logging as B
D=A.environ.get('GRIT_SERVER_PORT',8080)
E=A.environ.get('GRIT_LOG_LEVEL',B.WARN)
F=A.environ.get('GRIT_STATIC_DIR',A.path.join(A.path.dirname(__file__),C,C,'static'))