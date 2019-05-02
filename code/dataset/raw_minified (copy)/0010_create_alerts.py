from redash.models import db,Alert,AlertSubscription as A
if __name__=='__main__':
	with db.database.transaction():Alert.create_table();A.create_table()
	db.close_db(None)