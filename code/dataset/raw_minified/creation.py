def A(test=True,verbosity=1,autoclobber=False):
	'A wrapper over the Oracle `create_test_db` routine.'
	if not test:raise NotImplementedError('This uses `create_test_db` from db/backends/oracle/creation.py')
	from django.db import connection as A;A.creation.create_test_db(verbosity,autoclobber)