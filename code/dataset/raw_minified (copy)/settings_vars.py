from django.views.debug import get_safe_settings as D
from debug_toolbar.panels.settings_vars import SettingsVarsDebugPanel as A
class E(A):
	'Extends the Settings debug panel to enable logging.'
	def process_response(F,request,response):
		A=request;super(E,F).process_response(A,response)
		if getattr(A,'debug_logging',{}).get('ENABLED',False):
			G=D();B={}
			for (C,H) in G.items():
				if A.debug_logging['LOGGED_SETTINGS_RE'].search(C):B[C]=H
			A.debug_logging_stats['settings']=B