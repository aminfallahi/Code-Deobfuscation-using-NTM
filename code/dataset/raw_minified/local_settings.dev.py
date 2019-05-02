from settings import *
INSTALLED_APPS+='debug_toolbar','fixture_magic'
DEBUG_TOOLBAR_PATCH_SETTINGS=False
INTERNAL_IPS='127.0.0.1',
MIDDLEWARE_CLASSES+='debug_toolbar.middleware.DebugToolbarMiddleware',