from redash import models as A
if __name__=='__main__':B=A.Group.get(A.Group.name=='admin');B.permissions.append('super_admin');B.save()