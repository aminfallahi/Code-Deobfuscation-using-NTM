import os
from .completion_context import CompletionContext as A
class B(A):
	def __init__(A):
		C=False;super(B,A).__init__();A._command_line=os.getenv('CMDLINE_CONTENTS',C);A._char_index=int(os.getenv('CMDLINE_CURSOR_INDEX',0))
		if A._command_line is C:raise RuntimeError('Failed to configure from environment; Environment var CMDLINE_CONTENTS not set.')