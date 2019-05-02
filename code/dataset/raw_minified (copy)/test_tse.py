from TwitterSearch import *
import unittest,re
class TwitterSearchExceptionTest(unittest.TestCase):
	def test_TSE_common(self):
		' Tests basically the whole custom TwitterSearchException class ';regexpr=re.compile('^Error [0-9]{4}: [\\w :-]+$')
		for code in TwitterSearchException._error_codes:self.assertTrue(regexpr.match(str(TwitterSearchException(code))),'Odd string patterns detected')
		foo='someString';tse='%s'%TwitterSearchException(2000,foo);self.assertTrue(regexpr.match(tse)and tse[len(foo)*-1:]==foo)