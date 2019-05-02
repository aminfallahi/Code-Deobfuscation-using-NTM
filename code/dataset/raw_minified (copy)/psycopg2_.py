import psycopg2 as B
A=B.connect('dbname=test')
A.cursor
C=A.cursor()
C.fetchall