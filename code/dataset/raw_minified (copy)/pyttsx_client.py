F=print
import rospy,actionlib as C
from basics.msg import TalkAction as D,TalkGoal as E,TalkResult
rospy.init_node('speaker_client')
A=C.SimpleActionClient('speak',D)
A.wait_for_server()
B=E()
B.sentence='hello world, hello world, hello world, hello world'
A.send_goal(B)
A.wait_for_result()
F('[Result] State: %d'%A.get_state())
F('[Result] Status: %s'%A.get_goal_status_text())