'\nLegacy Email backend, docs at:\n    http://psa.matiasaguirre.net/docs/backends/email.html\n'
A='email'
from social.backends.legacy import LegacyAuth as B
class C(B):name=A;ID_KEY=A;REQUIRES_EMAIL_VALIDATION=True;EXTRA_DATA=[A]