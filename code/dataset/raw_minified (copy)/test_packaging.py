from changes import packaging as A
from .  import context as B,setup,teardown
def C():A.build_distributions(B)
def D():A.install_package(B)
def E():A.upload_package(B)
def F():A.install_from_pypi(B)