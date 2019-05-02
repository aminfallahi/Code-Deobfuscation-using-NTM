import tweepy as A
from SenseCells.tts import tts
def B(speech_text,consumer_key,consumer_secret,access_token,access_token_secret):B=speech_text.split();B.remove('tweet');D=' '.join(B).capitalize();C=A.OAuthHandler(consumer_key,consumer_secret);C.set_access_token(access_token,access_token_secret);E=A.API(C);E.update_status(status=D);tts('Your tweet has been posted')