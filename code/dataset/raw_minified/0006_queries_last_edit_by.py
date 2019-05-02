from playhouse.migrate import PostgresqlMigrator as B,migrate as C
from redash.models import db as A
from redash import models as D
if __name__=='__main__':
	A.connect_db();E=B(A.database)
	with A.database.transaction():C(E.add_column('queries','last_modified_by_id',D.Query.last_modified_by));A.database.execute_sql('UPDATE queries SET last_modified_by_id = user_id;')
	A.close_db(None)