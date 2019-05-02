from mixbox import entities,fields as A
import cybox.bindings.custom_object as B
from cybox.common import ObjectProperties as C,StructuredText as D
class E(C):_binding=B;_binding_class=B.CustomObjectType;_namespace='http://cybox.mitre.org/objects#CustomObject-1';_XSI_NS='CustomObj';_XSI_TYPE='CustomObjectType';custom_name=A.TypedField('custom_name');description=A.TypedField('Description',D)