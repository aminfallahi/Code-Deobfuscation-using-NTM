import pcd8544.lcd as A
def B():A.locate(0,0);A.text(map(chr,range(32,116)))
if __name__=='__main__':A.init();A.backlight(1);B()