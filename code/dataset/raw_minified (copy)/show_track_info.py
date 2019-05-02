import spotipy as B,sys,pprint as C
if len(sys.argv)>1:A=sys.argv[1]
else:A='spotify:track:0Svkvt5I79wficMFgaqEQJ'
D=B.Spotify()
E=D.track(A)
C.pprint(E)