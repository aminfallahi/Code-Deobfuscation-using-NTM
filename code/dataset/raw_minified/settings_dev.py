_C='MENU'
_B='crash'
_A='httplog'
from .settings_prod import *
INSTALLED_APPS+=_A,
MIDDLEWARE_CLASSES+='httplog.middleware.RequestResponseLoggingMiddleware',
HTTPLOG_URLNAMES=['update','sparkle_appcast',_B]
HTTPLOG_APPS=['omaha',_B,'sparkle']
SUIT_CONFIG[_C]=SUIT_CONFIG[_C]+({'app':_A,'label':_A,'icon':'icon-search'},)