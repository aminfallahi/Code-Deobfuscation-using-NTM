import smarter as A
from .models import Page
class B(A.GenericViews):'for test_automatic_view_discovery';model=Page
A.site.register(B,base_url='autodiscovery-test/',prefix='autodiscovery-test')