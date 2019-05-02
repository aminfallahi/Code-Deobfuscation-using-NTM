import SimpleCV as D,ImageTk as E,Tkinter as A,time
A.Tk()
F=D.Image('http://i.imgur.com/FTKqh.jpg')
B=E.PhotoImage(F.getPIL())
C=A.Label(image=B)
C.image=B
C.pack()
time.sleep(5)