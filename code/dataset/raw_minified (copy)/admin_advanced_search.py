A='advanced_search_form'
from django.contrib.admin.views.main import SEARCH_VAR as B
from django.template import Library as C
D=C()
@D.filter(name=A)
def E(context,cl):'\n    Displays a search form for searching the list.\n    ';return{A:context.get(A),'cl':cl,'show_result_count':cl.result_count!=cl.full_result_count,'search_var':B}