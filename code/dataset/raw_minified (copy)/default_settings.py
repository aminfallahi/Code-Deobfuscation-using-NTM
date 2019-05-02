B=hasattr
from django.conf import settings as A
C=False
D='DataImporter'
E=60*20
F=B(A,'DATA_IMPORTER_EXCEL_DECODER')and A.DATA_IMPORTER_EXCEL_DECODER or'cp1252'
G=B(A,'DATA_IMPORTER_DECODER')and A.DATA_IMPORTER_DECODER or'utf-8'