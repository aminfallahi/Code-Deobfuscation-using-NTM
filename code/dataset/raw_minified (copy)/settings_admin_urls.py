from django.core.urlresolvers import reverse as B
from django import template as A
C=A.Library()
@C.filter
def D(admin_change_list,type_name):A=admin_change_list;C='admin:%s_%s_%s'%(A.opts.app_label,A.opts.module_name,'add');D='typename=%(type)s%(popup)s'%dict(type=type_name,popup='_popup=1'if A.is_popup else'');return'%s?%s'%(B(C),D)