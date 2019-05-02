'\nDataFrame client for InfluxDB\n'
D=ImportError
__all__=['DataFrameClient']
try:import pandas as A;del A
except D as B:
	from .client import InfluxDBClient as C
	class DataFrameClient(C):
		def __init__(A,*C,**E):raise D("DataFrameClient requires Pandas which couldn't be imported: %s"%B)
else:from ._dataframe_client import DataFrameClient