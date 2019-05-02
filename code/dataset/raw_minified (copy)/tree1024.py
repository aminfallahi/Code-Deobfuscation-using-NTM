'\nCreate a 1024-host network, and run the CLI on it.\nIf this fails because of kernel limits, you may have\nto adjust them, e.g. by adding entries to /etc/sysctl.conf\nand running sysctl -p. Check util/sysctl_addon.\n'
from mininet.cli import CLI
from mininet.log import setLogLevel as B
from mininet.node import OVSSwitch as C
from mininet.topolib import TreeNet as D
if __name__=='__main__':B('info');A=D(depth=2,fanout=32,switch=C);A.run(CLI,A)