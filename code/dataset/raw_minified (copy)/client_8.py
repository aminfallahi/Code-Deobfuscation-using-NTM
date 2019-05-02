'\nGUI server.\n'
D='exec'
import client_1 as B
B.MAYAEXE=B.MAYAEXE.replace('mayabatch.exe','maya.exe')
import client_7 as A
A.COMMAND=A.SETCMD('_gui',A.ORIGCOMMAND)
if __name__=='__main__':C=A.create_client(A.start_process());A.sendrecv(C,(D,'import pymel.core as pmc'));A.sendrecv(C,(D,'pmc.polySphere()'));import time;time.sleep(20)