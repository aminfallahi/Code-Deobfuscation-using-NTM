import logging as A
D=A.getLogger(__name__)
from .bytemut import ByteMutFuzzer as B
class C(B):'\n    This fuzzer module randomly replaces single CR characters 0x0D with\n    random values. The percent of the selected bytes can be tweaked by\n    min_ratio and max_ratio. range_list specifies a range in the file to fuzz.\n    ';fuzzable_chars=[13]
E=C