from cassiopeia import baseriotapi as B
from ..  import int_test_handler as A
def D():print('dto/matchapi tests...');C()
def C():A.test_result(B.get_match(A.match_id))