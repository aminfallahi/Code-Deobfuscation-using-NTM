from django.test import TestCase as A
from data_importer.importers.base import DATA_IMPORTER_EXCEL_DECODER as B,DATA_IMPORTER_DECODER as C
class D(A):
	def test_data_importer_excel_decoder(A):A.assertEqual(B,'cp1252')
	def test_data_importer_decoder(A):A.assertEqual(C,'utf-8')