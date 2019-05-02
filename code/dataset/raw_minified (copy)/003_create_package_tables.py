from pypi_server.db.migrator import migration as A
from pypi_server.db.packages import Package as B,PackageFile as C,PackageVersion as D
@A(3)
def E(migrator,db):db.create_tables([B])
@A(4)
def F(migrator,db):db.create_tables([D])
@A(5)
def G(migrator,db):db.create_tables([C])