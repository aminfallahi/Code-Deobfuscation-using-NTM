from .workflow_rule import WorkflowRule
from .workflow_ruletarget import WorkflowRuleTarget
class A:
	'\n        TaskRouterConfig represents the filter and default_filter\n        of a workflow configuration of taskrouter\n    '
	def __init__(A,rules,default_target):A.filters=rules;A.default_filter=default_target
	def __repr__(A):return A.__dict__