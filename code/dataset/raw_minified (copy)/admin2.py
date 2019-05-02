from __future__ import division,absolute_import,unicode_literals
import djadmin2 as A
from .models import CaptionedFile as B,UncaptionedFile as C
A.default.register(B)
A.default.register(C)