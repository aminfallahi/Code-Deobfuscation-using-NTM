from mixbox import fields as A
import cybox.bindings.win_network_route_entry_object as B
from cybox.objects.network_route_entry_object import NetworkRouteEntry as D
from cybox.common import String as C
class E(D):_binding=B;_binding_class=B.WindowsNetworkRouteEntryObjectType;_namespace='http://cybox.mitre.org/objects#WinNetworkRouteEntryObject-2';_XSI_NS='WinNetworkRouteEntryObj';_XSI_TYPE='WindowsNetworkRouteEntryObjectType';nl_route_protocol=A.TypedField('NL_ROUTE_PROTOCOL',C);nl_route_origin=A.TypedField('NL_ROUTE_ORIGIN',C)