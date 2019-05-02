import subprocess as A
def B(path):B,C=A.Popen(['pdftotext','-layout','-table','-enc','UTF-8',path,'-'],stdout=A.PIPE).communicate();return B