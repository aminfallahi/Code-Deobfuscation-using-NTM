from mixbox import fields as A
import cybox.bindings.win_critical_section_object as B
from cybox.common import ObjectProperties as C,HexBinary as D,NonNegativeInteger as E
class F(C):_binding=B;_binding_class=B.WindowsCriticalSectionObjectType;_namespace='http://cybox.mitre.org/objects#WinCriticalSectionObject-2';_XSI_NS='WinCriticalSectionObj';_XSI_TYPE='WindowsCriticalSectionObjectType';address=A.TypedField('Address',D);spin_count=A.TypedField('Spin_Count',E)