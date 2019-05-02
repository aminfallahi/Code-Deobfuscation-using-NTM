'Auto-generated file, do not edit by hand. HR metadata'
F='112'
E=None
C='\\d{2,6}'
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as D
G=D(id='HR',country_code=E,international_prefix=E,general_desc=A(national_number_pattern='[19]\\d{1,5}',possible_number_pattern=C),toll_free=A(national_number_pattern='116(?:00[06]|111)',possible_number_pattern='\\d{6}',example_number='116000'),premium_rate=A(national_number_pattern=B,possible_number_pattern=B),emergency=A(national_number_pattern='1(?:12|9[2-4])|9[34]',possible_number_pattern=C,example_number=F),short_code=A(national_number_pattern='1(?:1[28]|16\\d{3}|987|9[2-5])|9[34]',possible_number_pattern=C,example_number=F),standard_rate=A(national_number_pattern=B,possible_number_pattern=B),carrier_specific=A(national_number_pattern=B,possible_number_pattern=B),short_data=True)