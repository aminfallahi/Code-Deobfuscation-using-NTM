from mixbox import fields as A
import cybox.bindings.win_waitable_timer_object as C
from cybox.common import String as B,ObjectProperties as D
class E(D):_binding=C;_binding_class=C.WindowsWaitableTimerObjectType;_namespace='http://cybox.mitre.org/objects#WinWaitableTimerObject-2';_XSI_NS='WinWaitableTimerObj';_XSI_TYPE='WindowsWaitableTimerObjectType';security_attributes=A.TypedField('Security_Attributes',B);name=A.TypedField('Name',B);type_=A.TypedField('Type',B)