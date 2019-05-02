from metakernel.tests.utils import get_kernel as C,get_log_text as D
def A():
	A=C();A.do_execute('%lsmagic');E=D(A)
	for B in '%cd %connect_info %download %edit %help %html %install_magic %javascript %kernel %kx %latex %load %lsmagic %magic %parallel %plot %pmap %px %python %reload_magics %restart %run %shell %macro %%debug %%file %%help %%html %%javascript %%kx %%latex %%processing %%px %%python %%shell %%show %%macro %%time'.split():assert B in E,"lsmagic didn't list '%s'"%B