from django import template as B
import md5
from gitology.utils import parse_date as C
A=B.Library()
@A.filter(name='md5')
def D(s):return md5.new(s).hexdigest()
@A.filter
def E(s):return C(s)
@A.inclusion_tag('comments.html',takes_context=True)
def F(context,document):A='form';return{'document':document,A:context[A]}