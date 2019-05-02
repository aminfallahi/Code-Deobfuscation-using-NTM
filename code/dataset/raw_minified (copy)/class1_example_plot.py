import matplotlib.pyplot as D
from hyperion.model import ModelOutput as E
from hyperion.util.constants import pc
F=E('class1_example.rtout')
B=F.get_sed(aperture=-1,distance=140.0*pc)
C=D.figure(figsize=(5,4))
A=C.add_subplot(1,1,1)
A.loglog(B.wav,B.val.transpose(),color='black')
A.set_xlim(0.03,2000.0)
A.set_ylim(2e-15,1e-08)
A.set_xlabel('$\\lambda$ [$\\mu$m]')
A.set_ylabel('$\\lambda F_\\lambda$ [ergs/cm$^2/s$]')
C.savefig('class1_example_sed.png',bbox_inches='tight')