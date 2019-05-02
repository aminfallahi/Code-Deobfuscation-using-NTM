C=''
import terminaloutput as A
E=A.modify_text_file
class B:
	val=0;mobtype=C
	def __init__(A,mobtype,val):
		D=val;B=mobtype;A.val=D;A.mobtype=B;A.art=E('mobs/%s_mobs/%s_art/mob%d_%s_art.txt'%(B,B,D,B));A.strings=E('mobs/%s_mobs/%s_strings/mob%d_%s_strings.txt'%(B,B,D,B));A.clean_strings=[]
		for F in A.strings:A.clean_strings.append(F.replace('#G',C).replace('G#',C).replace('#R',C).replace('R#',C))