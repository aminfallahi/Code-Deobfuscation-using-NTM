H=True
G=str
from argparse import ArgumentParser as C
from snapchat_bots import SnapchatBot as D
class E(D):
	def on_snap(A,sender,snap):A.post_story(snap)
if __name__=='__main__':A=C('Storifier Bot');A.add_argument('-u','--username',required=H,type=G,help='Username of the account to run the bot on');A.add_argument('-p','--password',required=H,type=G,help='Password of the account to run the bot on');B=A.parse_args();F=E(B.username,B.password);F.listen()