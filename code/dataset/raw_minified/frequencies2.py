import operator,collections as A
def B(word_list):B=A.Counter((A for A in word_list));return B.most_common(25)