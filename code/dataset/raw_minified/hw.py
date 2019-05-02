from pyglet import font as B,window as C
A=C.Window()
D=B.load('Helvetica',36)
E=B.Text(D,'Hello, World!')
while not A.has_exit:A.dispatch_events();A.clear();E.draw();A.flip()