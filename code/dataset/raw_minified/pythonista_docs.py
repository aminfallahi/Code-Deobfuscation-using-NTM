import sys,ui
if __name__=='__main__':B='file://{}/../Documentation/index.html'.format(sys.executable);A=ui.WebView(name='Pythonista Documentation');A.load_url(B);A.present()