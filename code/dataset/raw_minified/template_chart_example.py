class A(Report):
	template_chart=charts.TemplateChart(template='myapp/template_chart.html')
	def get_data_for_template_chart(C):A=[('Blue','Equus Caeruleus'),('Pink','Equus Roseus'),('Magical','Equus Magica')];B={'pony_types':A};return B