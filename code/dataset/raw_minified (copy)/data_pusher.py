from performanceplatform.client import DataSet as C
import logging as B
class A:
	def __init__(A,target_data_set_config,options):B=options;A.data_set_client=C.from_config(target_data_set_config);A.chunk_size=B.get('chunk-size',100);A.empty_data_set=B.get('empty-data-set',False)
	def push(A,data):
		if data:
			if A.empty_data_set:A.data_set_client.empty_data_set()
			A.data_set_client.post(data,chunk_size=A.chunk_size)
		else:B.info('Doing nothing - no data to push')