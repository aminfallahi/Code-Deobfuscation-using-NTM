__author__='daniel'
from sqlalchemy import Integer as C,Column as A,String as B
from sqlalchemy.orm import relationship as D
from lib.base import Base
class E(Base):__tablename__='racers';id=A(C,primary_key=True);name=A(B(50));hostname=A(B(50));location=A(B(50));trials=D('Trial',primaryjoin='Racer.id==Trial.racer_id')