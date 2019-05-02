import jinja2 as A
from django_jinja import library as B
from kitsune.sumo import parser as C
from kitsune.wiki.diff import BetterHtmlDiff as D
@B.global_function
def E(content_from,content_to):'Creates an HTML diff of the passed in content_from and content_to.';B=D();C=B.make_table(content_from.splitlines(),content_to.splitlines(),context=True);return A.Markup(C)
@B.global_function
def F(v):return A.Markup(C.generate_video(v))