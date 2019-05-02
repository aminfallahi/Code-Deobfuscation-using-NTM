from config.experiment_config_lib import ControllerConfig as A
from sts.topology import MeshTopology as B,BufferedPatchPanel
from sts.control_flow.interactive import Interactive as C
from sts.input_traces.input_logger import InputLogger as D
from sts.simulation_state import SimulationConfig as E
F='./pox.py --verbose openflow.of_01 --address=__address__ --port=__port__ openflow.discovery forwarding.l2_multi'
G=[A(F,cwd='pox',address='127.0.0.1',port=8888)]
H=B
I='num_switches=4'
J=E(controller_configs=G,topology_class=H,topology_params=I)
K=C(J,input_logger=D())