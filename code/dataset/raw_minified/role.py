A=dict
from chef.base import ChefObject as B
class C(B):'A Chef role object.';url='/roles';attributes={'description':str,'run_list':list,'default_attributes':A,'override_attributes':A,'env_run_lists':A}