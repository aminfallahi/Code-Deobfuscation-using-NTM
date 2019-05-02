from cassiopeia import baseriotapi as A
from ..  import int_test_handler as B
def C():'Checks that the request tracking works on requests with expected return code of 200';C=A.get_requests_count();B.test_result(A.get_match(B.match_id));B.test_result(A.get_requests_count()==(C[0]+1,C[1]+1))
def D():
	'Checks that the request tracking works on requests which raise exceptions';C=A.get_requests_count()
	try:A.get_champion(B.non_existent_champion_id)
	except:pass
	B.test_result(A.get_requests_count()==(C[0],C[1]+1))