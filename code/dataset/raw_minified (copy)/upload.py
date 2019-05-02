import os
from slackbot.bot import respond_to as A
from slackbot.utils import download_file as E,create_tmp_file as F
@A('upload \\<?(.*)\\>?')
def B(message,url):
	B=message;A=url;A=A.lstrip('<').rstrip('>');C=os.path.basename(A);B.reply('uploading {}'.format(C))
	if A.startswith('http'):
		with F()as D:E(A,D);B.channel.upload_file(C,D,'downloaded from {}'.format(A))
	elif A.startswith('/'):B.channel.upload_file(C,A)