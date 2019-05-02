'Auto-generated file, do not edit by hand. GI metadata'
G='150'
F='\\d{3}'
E='NA'
D=None
B='\\d{3,6}'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as C
H=C(id='GI',country_code=D,international_prefix=D,general_desc=A(national_number_pattern='[158]\\d{2,5}',possible_number_pattern=B),toll_free=A(national_number_pattern='1(?:00|16\\d{3}|23|47\\d|5[15]|9[2-4])|555',possible_number_pattern=B,example_number='100'),premium_rate=A(national_number_pattern=E,possible_number_pattern=E),emergency=A(national_number_pattern='1(?:12|9[09])',possible_number_pattern=F,example_number='112'),short_code=A(national_number_pattern='1(?:00|1(?:2|6(?:00[06]|1(?:1[17]|23))|8\\d{2})|23|4(?:1|7[014])|5[015]|9[02349])|555|8(?:008?|4[0-2]|88)',possible_number_pattern=B,example_number='116000'),standard_rate=A(national_number_pattern=G,possible_number_pattern=F,example_number=G),carrier_specific=A(national_number_pattern='1(?:18\\d{2}|23|51|9[2-4])|555|8(?:00|88)',possible_number_pattern='\\d{3,5}',example_number='123'),short_data=True)