from mixbox import fields as A
import cybox.bindings.gui_dialogbox_object as B
from cybox.common import String as C
from cybox.objects.gui_object import GUI
class D(GUI):_binding=B;_binding_class=B.GUIDialogboxObjectType;_namespace='http://cybox.mitre.org/objects#GUIDialogboxObject-2';_XSI_NS='GUIDialogBoxObj';_XSI_TYPE='GUIDialogboxObjectType';box_caption=A.TypedField('Box_Caption',C);box_text=A.TypedField('Box_Text',C)