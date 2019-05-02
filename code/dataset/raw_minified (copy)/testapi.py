C=None
import tw2.core as B,tw2.core.templating
from tw2.core.testbase import base as A
B.core.request_local=A.request_local_tst
def D():A._request_local={};A._request_id=C;tw2.core.templating.engine_name_cache={}
def E(requestid,mw=C):A._request_id=requestid;C=B.core.request_local();C.clear();C['middleware']=mw;return A.request_local_tst()