from mochi.utils.pycloader import get_module as B
A=B('add',file_path=__file__)
def C():assert A.add(2,2)==4
def D():assert A.add10(2)==12