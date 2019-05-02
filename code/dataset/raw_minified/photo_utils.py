from django import template as A
from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.encoding import smart_str,force_unicode
from django.utils.safestring import mark_safe
from django.template import loader as B
from niwi.utils import Singleton
C=A.Library()
@C.filter(name='firts_photo')
def D(album):A=album.photos.all()[:1].get();return B.render_to_string('photo/album_thumbnail.html',{'photo':A})