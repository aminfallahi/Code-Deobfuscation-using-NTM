from globals import *
import life as lfe,missions
def tick(life):
	for mission_id in life['missions'].keys():missions.do_mission(life,mission_id)