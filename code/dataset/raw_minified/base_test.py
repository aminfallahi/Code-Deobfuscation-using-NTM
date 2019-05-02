C=False
import unittest as A
from models.appointment import Appointment as B
class D(A.TestCase):
	def setUp(A):from reminders import app as B,db;A.app=B;A.db=db;A.celery=B.celery();A.test_client=B.flask_app.test_client();A.app.flask_app.config['WTF_CSRF_ENABLED']=C
	def tearDown(A):A.db.session.query(B).delete();A.db.session.commit();A.celery.control.purge();A.celery.conf.CELERY_ALWAYS_EAGER=C