import pychromecast as A
def B():B=A.get_chromecast();C=B.media_controller;B.wait();C.play_media('http://commondatastorage.googleapis.com/gtv-videos-bucket/'+'sample/BigBuckBunny.mp4','video/mp4')
def C():B=A.get_chromecast();C=B.media_controller;B.wait();C.stop()