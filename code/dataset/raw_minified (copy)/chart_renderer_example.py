A=classmethod
from report_tools.renderers import ChartRenderer as B
class C(B):
	@A
	def render_piechart(cls,chart_id,options,data,renderer_options):A=cls;return"<div id='%s' class='placeholder'>Pie Chart</div>"%chart_id
	@A
	def render_columnchart(cls,chart_id,options,data,renderer_options):A=cls;return"<div id='%s' class='placeholder'>Column Chart</div>"%chart_id
	@A
	def render_barchart(cls,chart_id,options,data,renderer_options):A=cls;return"<div id='%s' class='placeholder'>Bar Chart</div>"%chart_id
	@A
	def render_linechart(cls,chart_id,options,data,renderer_options):A=cls;return"<div id='%s' class='placeholder'>Line Chart</div>"%chart_id