from mixbox import entities as C,fields as A
import cybox.bindings.cybox_core as B
class D(C.Entity):_binding=B;_binding_class=B.FrequencyType;_namespace='http://cybox.mitre.org/cybox-2';rate=A.TypedField('rate');units=A.TypedField('units');scale=A.TypedField('scale');trend=A.TypedField('trend')