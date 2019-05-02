import random as C
def A(status,settings):
	F=' ';E='utf-8';A=status.text.lower().replace('@'+settings.username,'').strip();A=A.encode(E);B=A.split(F)
	if B[0]=='choose':D=[A.strip()for A in F.join(B[1:]).split(',')];return dict(response=C.choice(D).decode(E))