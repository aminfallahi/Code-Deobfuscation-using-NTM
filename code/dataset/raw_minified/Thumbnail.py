B=True
from google.appengine.ext import ndb as A
class C(A.Model):image=A.BlobProperty();mimetype=A.StringProperty();developer_id=A.IntegerProperty();thumb_type=A.IntegerProperty();created_at=A.DateTimeProperty(auto_now_add=B);updated_at=A.DateTimeProperty(auto_now=B)