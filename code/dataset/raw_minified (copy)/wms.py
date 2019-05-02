C=True
B=False
from django.contrib.gis.db import models as A
class D(A.Model):name=A.CharField(max_length=255,blank=B)
class E(A.Model):collection=A.ForeignKey(D,null=B);location=A.TextField(blank=B,null=B);checksum=A.CharField(max_length=32,blank=B,null=B);name=A.CharField(max_length=255,blank=B,null=B,db_index=C);human_name=A.TextField(blank=C,null=C,db_index=C);extent=A.PolygonField(srid=4326)
class F(A.Model):dataset=A.ForeignKey(E);name=A.CharField(max_length=255,db_index=C);human_name=A.TextField(blank=C,null=C,db_index=C);extent=A.PolygonField(srid=4326)