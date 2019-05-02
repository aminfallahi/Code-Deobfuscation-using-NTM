'\nResource traversal integration with L{twisted.cred} to allow for\nauthentication and authorization of HTTP requests.\n'
from twisted.web._auth.wrapper import HTTPAuthSessionWrapper
from twisted.web._auth.basic import BasicCredentialFactory
from twisted.web._auth.digest import DigestCredentialFactory
__all__=['HTTPAuthSessionWrapper','BasicCredentialFactory','DigestCredentialFactory']