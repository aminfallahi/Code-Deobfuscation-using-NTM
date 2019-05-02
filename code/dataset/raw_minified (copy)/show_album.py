import spotipy as B,sys,pprint as C
if len(sys.argv)>1:A=sys.argv[1]
else:A='spotify:artist:3jOstUTkEu2JkjvRdBA5Gu'
D=B.Spotify()
E=D.artist(A)
C.pprint(E)