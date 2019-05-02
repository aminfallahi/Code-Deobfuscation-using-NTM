from cassiopeia import baseriotapi as B
from ..  import int_test_handler as A
def D():print('dto/currentgameapi tests...');C()
def C():A.test_result(B.get_current_game(A.summoner_id))