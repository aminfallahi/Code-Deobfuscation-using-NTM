import pytest
from okcupyd import json_search as B
from tests import util
@util.use_cassette
def A():
	for A in B.SearchFetchable()[:4]:assert A.username;assert A.details.status