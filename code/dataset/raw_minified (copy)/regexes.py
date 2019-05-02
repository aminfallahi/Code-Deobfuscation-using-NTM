from __future__ import unicode_literals
import re as A
B=set([('spaces',A.compile('\\s+',A.U)),('word',A.compile('\\w+',A.U)),('mac',A.compile('^(ma?c)(\\w+)',A.I|A.U)),('initial',A.compile('^(\\w\\.|[A-Z])?$',A.U)),('nickname',A.compile('\\s*?[\\("](.+?)[\\)"]',A.U)),('roman_numeral',A.compile('^(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$',A.I|A.U))])
'\nAll regular expressions used by the parser are precompiled and stored in the config.\n'