from __future__ import absolute_import,unicode_literals
from pre_commit_hooks.check_ast import check_ast as A
from testing.util import get_resource_path as B
def C():C=A([B('cannot_parse_ast.notpy')]);assert C==1
def D():B=A([__file__]);assert B==0