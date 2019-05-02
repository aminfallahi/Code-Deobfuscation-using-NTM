class A:
	class ConfigError(Exception):
		def __init__(A,msg):A.msg=msg
		def __str__(A):return A.msg
	def get_config_dict(A):raise NotImplementedError()