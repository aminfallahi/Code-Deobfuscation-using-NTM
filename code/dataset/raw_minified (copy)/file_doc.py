'\nCreated on Mar 15, 2013\n\n@organization: cert.org\n'
try:from couchdb.mapping import TextField as A,IntegerField as B,Document as C
except ImportError as D:pass
class E(C):doctype=A(default='File');filename=A();extension=A();sha1=A();size_in_bytes=B();derived_from_file_id=A()