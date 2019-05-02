from connexion.decorators.metrics import UWSGIMetricsCollector as D
from mock import MagicMock as A
def B(monkeypatch):
	B=monkeypatch;E=D('/foo/bar/<param>','get')
	def F():A=None;return A,418,A
	G=E(F);C=A();B.setattr('flask.request',A());B.setattr('connexion.decorators.metrics.uwsgi_metrics',C);G();assert C.timer.call_args[0][:2]==('connexion.response','418.GET.foo.bar.{param}')