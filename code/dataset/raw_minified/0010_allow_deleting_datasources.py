from playhouse.migrate import PostgresqlMigrator as A,migrate as B
from redash.models import db
if __name__=='__main__':
	db.connect_db();C=A(db.database)
	with db.database.transaction():B(C.drop_not_null('queries','data_source_id'))
	db.close_db(None)