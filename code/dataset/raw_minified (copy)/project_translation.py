from modeltranslation.translator import translator as A,TranslationOptions as B
from .test_app.models import Other
class C(B):fields='name',
A.register(Other,C)