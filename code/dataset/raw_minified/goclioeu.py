from social.backends.goclio import GoClioOAuth2 as A
class B(A):
	name='goclioeu';AUTHORIZATION_URL='https://app.goclio.eu/oauth/authorize/';ACCESS_TOKEN_URL='https://app.goclio.eu/oauth/token/'
	def user_data(A,access_token,*B,**C):'Loads user data from service';return A.get_json('https://app.goclio.eu/api/v2/users/who_am_i',params={'access_token':access_token})