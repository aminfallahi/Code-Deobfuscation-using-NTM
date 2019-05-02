from django.db.utils import OperationalError as A
from solo.admin import SingletonModelAdmin
from resumator.models import BasicInformation as B
from resumator.models import Settings as C
try:D=B.get_solo()
except A:pass
try:E=C.get_solo()
except A:pass