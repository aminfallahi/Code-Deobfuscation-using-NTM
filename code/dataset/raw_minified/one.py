from venusian.tests.fixtures import decorator as A
from venusian.tests.fixtures.import_and_scan.two import twofunction as B
@A(function=True)
def C(request):A=request;B(A);return A