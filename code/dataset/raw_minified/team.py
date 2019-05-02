from cassiopeia import baseriotapi as B
from ..  import int_test_handler as A
def E():print('dto/team tests...');C();D()
def C():A.test_result(B.get_teams_by_summoner_id(A.summoner_id))
def D():A.test_result(B.get_teams_by_id(A.team_id))