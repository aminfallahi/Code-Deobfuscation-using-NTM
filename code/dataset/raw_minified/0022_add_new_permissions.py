from redash import models as A
if __name__=='__main__':
	with A.db.database.transaction():
		C=A.Group.select(A.Group.id,A.Group.permissions).where(A.Group.name=='default')
		for B in C:B.permissions.append('list_dashboards');B.permissions.append('list_alerts');B.permissions.append('list_data_sources');B.save(only=[A.Group.permissions])