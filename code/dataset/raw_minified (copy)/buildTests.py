import devon.make,devon.web,sys
def main(request):request.servePage('process.html',globals(),locals())
def process(request):devon.web.buildProcess(request,'buildTests')