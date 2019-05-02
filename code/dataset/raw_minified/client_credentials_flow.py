from spotipy.oauth2 import SpotifyClientCredentials as A
import spotipy as B,pprint as C
D=A()
E=B.Spotify(client_credentials_manager=D)
F='Muse'
G=E.search(F)
C.pprint(G)