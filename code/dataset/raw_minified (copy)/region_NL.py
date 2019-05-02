'Auto-generated file, do not edit by hand. NL metadata'
E='\\d{3,6}'
D=None
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as C
F=C(id='NL',country_code=D,international_prefix=D,general_desc=A(national_number_pattern='[19]\\d{2,5}',possible_number_pattern=E),toll_free=A(national_number_pattern='116(?:00[06]|123)',possible_number_pattern='\\d{6}',example_number='116000'),premium_rate=A(national_number_pattern=B,possible_number_pattern=B),emergency=A(national_number_pattern='112|911',possible_number_pattern='\\d{3}',example_number='112'),short_code=A(national_number_pattern='1(?:1(?:2|6(?:00[06]|123))|833)|911',possible_number_pattern=E,example_number='1833'),standard_rate=A(national_number_pattern=B,possible_number_pattern=B),carrier_specific=A(national_number_pattern=B,possible_number_pattern=B),short_data=True)