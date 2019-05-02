A='example.com'
import httplib as B
C=B.HTTPSConnection(A)
import http.client
C=http.client.HTTPSConnection(A)
import six
six.moves.http_client.HTTPSConnection(A)