from AlphaGo.preprocessing.game_converter import game_converter as B
from cProfile import Profile as C
A=C()
D=['board','turns_since','liberties','capture_size','self_atari_size','liberties_after','sensibleness','zeros']
E=B(D)
F='tests/test_data/sgf/Lee-Sedol-vs-AlphaGo-20160309.sgf',19
def G():
	for A in E.convert_game(*F):0
A.runcall(G)
A.dump_stats('bench_results.prof')