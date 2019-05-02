'\nWrapper class for use with cgi.FieldStorage types for file uploads\n'
from __future__ import absolute_import
import cgi
def A(fs):return fs if fs.filename else None