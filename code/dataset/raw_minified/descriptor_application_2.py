from cleo import Application as A
from .descriptor_command_1 import DescriptorCommand1 as B
from .descriptor_command_2 import DescriptorCommand2 as C
class D(A):
	def __init__(A):super(D,A).__init__('My Cleo application','v1.0');A.add(B());A.add(C())