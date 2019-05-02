from __future__ import absolute_import
from svtplay_dl.utils import is_py2 as A
if A:from urllib import quote,unquote_plus,quote_plus;from urlparse import urlparse,parse_qs,urljoin
else:from urllib.parse import quote,unquote_plus,quote_plus,urlparse,parse_qs,urljoin