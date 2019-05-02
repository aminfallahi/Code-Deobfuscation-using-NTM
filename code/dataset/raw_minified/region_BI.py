'Auto-generated file, do not edit by hand. BI metadata'
H='117'
G='\\d{3,4}'
F=None
D='\\d{3}'
C='611'
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as E
I=E(id='BI',country_code=F,international_prefix=F,general_desc=A(national_number_pattern='[16-9]\\d{2,3}',possible_number_pattern=G),toll_free=A(national_number_pattern=C,possible_number_pattern=D,example_number=C),premium_rate=A(national_number_pattern=B,possible_number_pattern=B),emergency=A(national_number_pattern='11[237]',possible_number_pattern=D,example_number=H),short_code=A(national_number_pattern='1(?:1\\d|5[2-9]|6[0-256])|611|7(?:10|77|979)|8[28]8|900',possible_number_pattern=G,example_number=H),standard_rate=A(national_number_pattern=B,possible_number_pattern=B),carrier_specific=A(national_number_pattern='611|7(?:10|77)|888|900',possible_number_pattern=D,example_number=C),short_data=True)