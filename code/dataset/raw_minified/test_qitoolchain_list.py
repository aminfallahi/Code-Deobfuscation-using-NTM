B='list'
from qibuild.test.conftest import QiBuildAction
from qitoolchain.test.conftest import QiToolchainAction
def A(qitoolchain_action,record_messages):qitoolchain_action(B);assert record_messages.find('No toolchain yet')
def C(qitoolchain_action,record_messages):A=qitoolchain_action;A('create','foo');A(B);assert record_messages.find('\\* foo')