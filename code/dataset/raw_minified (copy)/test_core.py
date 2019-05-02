import warnings as B
from dotenv import load_dotenv as C
def A():
	with B.catch_warnings(record=True)as A:C('.does_not_exist');assert len(A)==1;assert A[0].category is UserWarning;assert str(A[0].message)=="Not loading .does_not_exist - it doesn't exist."