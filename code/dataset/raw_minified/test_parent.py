'Test givens declared in the parent conftest and plugin files.\n\nCheck the parent givens are collected and overriden in the local conftest.\n'
from pytest_bdd.steps import get_step_fixture_name as A,WHEN
def B(parent,overridable):'Test parent given is collected.\n\n    Both fixtures come from the parent conftest.\n    ';A='parent';assert parent==A;assert overridable==A
def C(request):'Test when step defined in the parent conftest.';request.getfuncargvalue(A('I use a when step from the parent conftest',WHEN))