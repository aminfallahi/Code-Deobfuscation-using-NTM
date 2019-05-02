from flask import Flask
from flask_mysqldb import MySQL
A=Flask(__name__)
B=MySQL(A)
@A.route('/')
def C():A=B.connection.cursor();A.execute('SELECT user, host FROM mysql.user');C=A.fetchall();return str(C)
if __name__=='__main__':A.run(debug=True)