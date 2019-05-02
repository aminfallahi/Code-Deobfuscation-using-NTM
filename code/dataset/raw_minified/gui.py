from config.experiment_config_lib import ControllerConfig as A
from sts.topology import FatTree as B,BufferedPatchPanel
from sts.control_flow.interactive import Interactive as C
from sts.input_traces.input_logger import InputLogger as D
from sts.simulation_state import SimulationConfig as E
F='./pox.py --no-cli --verbose openflow.of_01 --address=__address__ --port=__port__ sts.syncproto.pox_syncer samples.topo forwarding.l2_learning'
G=[A(F,cwd='pox',address='127.0.0.1',port=8888,sync='tcp:localhost:18888')]
H=B
I='num_pods=2, gui=True'
J='dataplane_traces/ping_pong_same_subnet.trace'
K=E(controller_configs=G,topology_class=H,topology_params=I,dataplane_trace=J)
L=C(K,input_logger=D())