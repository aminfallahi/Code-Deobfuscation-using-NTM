from fabric.api import settings as E
from fabric import tasks as C
from depl import deploy as D
A='localhost'
def B():
	G='pacman';F='yum'
	with E(hosts=[A]):B=C.execute(D.package_manager.system);assert B[A]in['apt',F,G];B=C.execute(D.package_manager._manager);assert B[A]in['apt-get',F,G]