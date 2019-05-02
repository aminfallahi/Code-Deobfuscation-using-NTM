D='op2_prop'
from cloudify import ctx
from cloudify.state import ctx_parameters as B
from testenv.utils import update_storage as C
with C(ctx)as A:A[D]=ctx.instance.runtime_properties[D];A['op1_called_with_property']=B.property