'\nHelios URLs for Election related stuff\n\nBen Adida (ben@adida.net)\n'
from django.conf.urls import *
from helios.stats_views import *
urlpatterns=patterns('',('^$',home),('^force-queue$',force_queue),('^elections$',elections),('^problem-elections$',recent_problem_elections),('^recent-votes$',recent_votes))