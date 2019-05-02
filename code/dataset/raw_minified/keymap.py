import os
from suplemon import config as A
class B(A.ConfigModule):
	'Shortcut to openning the keymap config file.'
	def init(A):A.config_name='keymap.json';A.config_default_path=os.path.join(A.app.path,'config',A.config_name);A.config_user_path=A.app.config.keymap_path()
C={'class':B,'name':'keymap'}