from substanced.catalog.indexes import PathIndex as C
from substanced.util import get_dotted_name as D
from substanced.objectmap import find_objectmap as E
def A(root,registry):
	A=E(root);F=A.get_extent(D(C))
	for G in F:B=A.object_for(G);B._not_indexed=A.family.IF.TreeSet(B._not_indexed)
def B(config):config.add_evolution_step(A)