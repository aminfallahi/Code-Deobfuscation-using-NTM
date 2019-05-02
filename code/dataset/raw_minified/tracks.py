G=' '
import spotipy as A,sys
B=A.Spotify()
if len(sys.argv)>1:
	C=G.join(sys.argv[1:]);D=B.search(q=C,limit=20)
	for (E,F) in enumerate(D['tracks']['items']):print(G,E,F['name'])