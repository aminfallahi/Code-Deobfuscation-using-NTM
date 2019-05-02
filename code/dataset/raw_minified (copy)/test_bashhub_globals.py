from bashhub.bashhub import bashhub_globals as A
def B():B='[a-2]';C='(filter_me|ssh)';assert False==A.is_valid_regex(B);assert True==A.is_valid_regex(C)