from cassiopeia import baseriotapi as A
from ..  import int_test_handler as B
def E():print('dto/status tests...');C();D()
def C():B.test_result(A.get_shards())
def D():B.test_result(A.get_shard())