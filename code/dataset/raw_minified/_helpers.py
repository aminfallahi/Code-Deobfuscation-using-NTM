C=ord
B=dict
def A(filename):D=[' ','-'];E=['.','!',':',';','/',',','(',')','[',']','{','}','&','"',"'",'*','\\','<','>'];A=B(((C(A),'')for A in E));A.update(B(((C(A),'_')for A in D)));return filename.translate(A)