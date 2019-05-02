from reportlab.platypus import SimpleDocTemplate as B,Paragraph as C
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.styles import getSampleStyleSheet as D
from reportlab.lib.enums import TA_JUSTIFY as E
def A():F=D();G=B('phello.pdf');A=F['Normal'];A.alignment=E;H=C('PADDING PADDING PADDING PADDING PADDING PADDING The computer will always be better than you at parsing SQL\nand the bad guys have years of experience finding and using <a href="http://en.wikipedia.org/wiki/SQL_injection" color="navy">SQL\ninjection attacks</a><a name="sql-injection-attacks"/> in\nways you never even thought possible.',A);G.build([H])
A()