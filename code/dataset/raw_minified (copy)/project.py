import os,qitest.conf
class A:
	def __init__(A,qitest_json):B=qitest_json;A.name=None;A.tests=qitest.conf.parse_tests(B);A.sdk_directory=os.path.dirname(B)