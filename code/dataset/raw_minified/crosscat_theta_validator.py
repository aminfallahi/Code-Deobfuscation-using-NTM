import json,jsonschema as A,pkgutil as B
class C:
	def __init__(A):C=B.get_data('bayeslite.metamodels','crosscat_theta.schema.json');A.schema=json.loads(C)
	def validate(B,obj):'Validate a Crosscat theta object.\n\n        The object should the json-deserialized version of something that would\n        be stored in the theta_json column of the bayesdb_crosscat_theta\n        column. Raises an exception when validation fails.';A.validate(obj,B.schema)