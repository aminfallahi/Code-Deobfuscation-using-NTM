from pypi_server.db.migrator import migration as A
from pypi_server.db.users import Users
@A(2)
def B(migrator,db):A='admin';Users(login=A,password=A,email='admin@example.net',is_admin=True).save()