B=None
from .identifier import Identifier as A
class C:
	def __init__(A,old_column_name,column,changed_properties=B,from_column=B):A.old_column_name=old_column_name;A.column=column;A.changed_properties=changed_properties;A.from_column=from_column
	def has_changed(A,property_name):return property_name in A.changed_properties
	def get_old_column_name(B):return A(B.old_column_name)