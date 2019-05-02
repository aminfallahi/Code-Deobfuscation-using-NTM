from django.conf import settings as A
if getattr(A,'EVERNOTE_DEBUG',False):from social.backends.evernote import EvernoteSandboxOAuth as B
else:from social.backends.evernote import EvernoteOAuth as B