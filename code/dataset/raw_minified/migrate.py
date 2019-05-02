from app import engine as A
from models import Base
from social.apps.webpy_app.models import SocialBase as B
if __name__=='__main__':Base.metadata.create_all(A);B.metadata.create_all(A)