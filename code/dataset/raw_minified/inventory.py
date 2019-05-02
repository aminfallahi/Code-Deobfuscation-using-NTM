import globals,sys,os,terminaloutput as A
C=A.modify_text_file
class B:
	val=0;art=''
	def __init__(A,val):B=val;A.val=B;A.art=C('inventory/art/inv%d_art.txt'%B);A.desc=C('inventory/descriptions/inv%d_description.txt'%B)