import pytest as B
from growler.http.status import Status as A
@B.mark.parametrize('code, phrase',[(100,'Continue'),(200,'OK'),(403,'Forbidden'),(404,'Not Found'),(500,'Internal Server Error')])
def C(code,phrase):B=phrase;assert A.phrase_dict[code]==B;assert A.Phrase(code)==B