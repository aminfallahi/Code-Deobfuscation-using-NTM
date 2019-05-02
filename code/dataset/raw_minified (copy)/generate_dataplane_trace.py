import os,sys
sys.path.append(os.path.join(os.path.dirname(__file__),'..'))
from sts.dataplane_traces.trace_generator import generate_example_trace_same_subnet as A
A(num_switches=2)