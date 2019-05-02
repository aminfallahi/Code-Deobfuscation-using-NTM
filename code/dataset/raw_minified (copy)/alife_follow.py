from globals import *
import life as lfe,judgement,movement,sight
def tick(life):
	A=False;_guard=judgement.get_target_to_guard(life)
	if _guard:return movement.find_target(life,_guard,follow=A,distance=sight.get_vision(life)*0.25,call=A)
	return movement.find_target(life,judgement.get_target_to_follow(life),follow=True,call=A)