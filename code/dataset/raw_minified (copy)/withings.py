A='userid'
from social.backends.oauth import BaseOAuth1 as B
class C(B):
	name='withings';AUTHORIZATION_URL='https://oauth.withings.com/account/authorize';REQUEST_TOKEN_URL='https://oauth.withings.com/account/request_token';ACCESS_TOKEN_URL='https://oauth.withings.com/account/access_token';ID_KEY=A
	def get_user_details(B,response):'Return user details from Withings account';return{A:response['access_token'][A],'email':''}