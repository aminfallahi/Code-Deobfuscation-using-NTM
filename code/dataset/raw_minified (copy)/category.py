C=True
from venusian.tests.fixtures import categorydecorator as A,categorydecorator2 as B
@A(function=C)
def D(request):return request
@B(function=C)
def E(request):return request