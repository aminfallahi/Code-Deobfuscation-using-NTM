from cassiopeia import baseriotapi as B
from ..  import int_test_handler as A
def D():print('dto/gameapi tests...');C()
def C():A.test_result(B.get_recent_games(A.summoner_id))