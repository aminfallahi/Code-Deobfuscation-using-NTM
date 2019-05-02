from subprocess import call
def A():'\n    requires node.js and the CoffeeScript module for to be installed.\n    ';call(['coffee','--compile','--output','static/js/','coffee/'],shell=True)
if __name__=='__main__':A()