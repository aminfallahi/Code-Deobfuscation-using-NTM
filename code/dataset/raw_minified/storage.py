'\nIn-memory file storage for tests.\n\n'
import urlparse as A
from django.conf import settings as B
from django.utils.encoding import filepath_to_uri as C
import inmemorystorage as D
class E(D.InMemoryStorage):
	'An in-memory Django file storage backend, for tests.'
	def url(D,name):"In-memory files aren't actually URL-accessible; we'll pretend.";return A.urljoin(B.MEDIA_URL,C(name))