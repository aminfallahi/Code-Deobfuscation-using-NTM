A=True
from userena.models import UserenaBaseProfile as B
class C(B):' A profile used for testing. ';GENDER_CHOICES=(1,_('Male')),(2,_('Female'));gender=models.PositiveSmallIntegerField(_('gender'),choices=GENDER_CHOICES,blank=A,null=A);website=models.URLField(_('website'),blank=A);location=models.CharField(_('location'),max_length=255,blank=A);about_me=models.TextField(_('about me'),blank=A)