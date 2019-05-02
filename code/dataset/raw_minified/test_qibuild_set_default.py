import qibuild.config
from qibuild.test.conftest import TestBuildWorkTree as B
def A(qibuild_action):A='foo';qibuild.config.add_build_config(A);qibuild_action('set-default',A);C=B();assert C.build_config.active_build_config.name==A