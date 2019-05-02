'Startup.'
C=print
import os
if __name__=='__main__':
	A=raw_input('Enter an option: [billing | inventory | shipping] ');A=A.strip();C('You chose: {}'.format(A));B=os.getcwd()
	if A=='billing':C('Starting billing service');os.system('python {}/billing_svc/app.py'.format(B))
	elif A=='inventory':C('Starting inventory service');os.system('python {}/inventory_svc/app.py'.format(B))
	elif A=='shipping':C('Starting shipping service');os.system('python {}/shipping_svc/app.py'.format(B))