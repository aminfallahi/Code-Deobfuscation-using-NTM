'Log all messages to the database\n\nOnly active if the LIMBO_LOG_EVERYTHING environment variable is set'
import os
B=os.environ.get('LIMBO_LOG_EVERYTHING',False)
def A(msg,server):
	A=msg
	if B:server.query('INSERT INTO log VALUES (?, ?, ?, ?, ?)',A['text'],A['user'],A['ts'],A['team'],A['channel'])
def C(server):
	if B:server.query('\nCREATE TABLE IF NOT EXISTS log\n    (msg STRING, sender STRING, time STRING, team STRING, channel STRING)\n')