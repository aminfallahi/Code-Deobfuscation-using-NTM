A=set
from pydsa import bfs
def B():G='D';F='F';E='E';D='C';C='B';B='A';H={B:A([C,D]),C:A([B,G,E]),D:A([B,F]),G:A([C]),E:A([C,F]),F:A([D,E])};assert bfs(H,B)==A([B,D,C,F,E,G])