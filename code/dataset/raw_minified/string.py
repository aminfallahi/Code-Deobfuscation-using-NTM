from __future__ import absolute_import,unicode_literals,division
import re
def A(value):'Dasherizes the passed value.';A=value;A=A.strip();A=re.sub('([A-Z])','-\\1',A);A=re.sub('[-_\\s]+','-',A);A=re.sub('^-','',A);A=A.lower();return A