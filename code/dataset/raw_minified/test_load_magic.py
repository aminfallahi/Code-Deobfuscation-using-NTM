from metakernel.tests.utils import get_kernel as A
def B():B=A();C=B.do_execute('%%load %s'%__file__);assert'def test_load_magic'in C['payload'][0]['text']