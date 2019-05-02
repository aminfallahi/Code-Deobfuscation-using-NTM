'\nViews for image content objects.\n'
from kotti_image.views import _load_image_scales as A,image_scales as B,ImageView as C,includeme as D
from zope.deprecation import deprecated as E
__=A,B,C,D
E(('_load_image_scales','image_scales','ImageView','includeme'),'Image was outfactored to the kotti_image package.  Please import from there.')