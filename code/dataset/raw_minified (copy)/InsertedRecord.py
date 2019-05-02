from clear_table import clear_table as B
class A:
	'Inserts and commits a record and removes it at the end of\n    a test no matter what happens.\n    \n    '
	def __init__(A,db,table,data):A.db=db;A.table=table;A.data=data
	def __enter__(A):A.table.insert(**A.data);A.db.commit()
	def __exit__(A,type,value,traceback):B(A.db,A.table)