from django.shortcuts import render as B
from myapp.reports import MyReport as A
from report_tools.views import ReportView as C
class D(C):
	def get_report(B,request):return A()
	def get(C,request):A=request;D='myapp/my_report.html';E={'report':C.get_report(A)};return B(A,D,E)