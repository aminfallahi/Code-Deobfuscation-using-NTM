import os
from aiotg import Bot
A=Bot(os.environ['API_TOKEN'])
@A.command('/getimage')
def B(chat,match):return chat.send_photo(photo=open('cc.large.png','rb'),caption='Creative commons')
if __name__=='__main__':A.run()