from tenant_schemas.management.commands import TenantWrappedCommand as A
from django.contrib.auth.management.commands import createsuperuser as B
class C(A):COMMAND=B.Command