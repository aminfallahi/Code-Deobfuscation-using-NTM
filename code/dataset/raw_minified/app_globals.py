"The application's Globals object"
from beaker.cache import CacheManager as A
from beaker.util import parse_cache_config_options as B
class C:
	'Globals acts as a container for objects available throughout the\n    life of the application\n\n    '
	def __init__(C,config):"One instance of Globals is created during application\n        initialization and is available during requests via the\n        'app_globals' variable\n\n        ";C.cache=A(**B(config))