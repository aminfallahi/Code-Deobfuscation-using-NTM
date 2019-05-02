__author__='jon'
from ladder.models import Season as A
def B(request):'\n    Generates the urls for the top navigation\n    ';B=A.objects.order_by('-start_date')[1:5];C=A.objects.latest('start_date');D=A.objects.count();return{'navigation':B,'season_count':D,'season_first':C}