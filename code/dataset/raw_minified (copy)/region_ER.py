'Auto-generated file, do not edit by hand. ER metadata'
E=None
C='\\d{3,6}'
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as D
F=D(id='ER',country_code=E,international_prefix=E,general_desc=A(national_number_pattern='[12]\\d{2,5}',possible_number_pattern=C),toll_free=A(national_number_pattern=B,possible_number_pattern=B),premium_rate=A(national_number_pattern=B,possible_number_pattern=B),emergency=A(national_number_pattern='1(?:1[2-46]|2(?:4422|7799))|2(?:0(?:1(?:606|917)|2(?:099|914)))',possible_number_pattern=C,example_number='113'),short_code=A(national_number_pattern='1(?:1[2-6]|2(?:4422|7799))|2(?:0(?:1(?:606|917)|2(?:099|914)))',possible_number_pattern=C,example_number='114'),standard_rate=A(national_number_pattern=B,possible_number_pattern=B),carrier_specific=A(national_number_pattern=B,possible_number_pattern=B),short_data=True)