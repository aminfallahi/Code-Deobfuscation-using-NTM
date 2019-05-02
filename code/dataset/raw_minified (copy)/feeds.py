from django.utils.feedgenerator import Atom1Feed as A,Rss201rev2Feed as C
from philo.utils.registry import Registry as D
E=A
B=D()
B.register(A,verbose_name='Atom')
B.register(C,verbose_name='RSS')