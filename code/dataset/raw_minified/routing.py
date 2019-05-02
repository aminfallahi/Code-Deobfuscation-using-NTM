from __future__ import absolute_import,unicode_literals
from channels.routing import route as A
from .  import consumers as B
C=[A('websocket.connect',B.ws_connect,path='^/nyt/?$'),A('websocket.disconnect',B.ws_disconnect),A('websocket.receive',B.ws_receive)]