from eventlet import patcher
from eventlet.green import socket
from eventlet.green import select
from eventlet.green import threading
patcher.inject('SocketServer',globals(),('socket',socket),('select',select),('threading',threading))