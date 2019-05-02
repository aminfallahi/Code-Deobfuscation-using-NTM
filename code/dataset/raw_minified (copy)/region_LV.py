'Auto-generated file, do not edit by hand. LV metadata'
G='\\d{4}'
F='1181'
E='112'
D='\\d{2,6}'
C=None
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as B
H=B(id='LV',country_code=C,international_prefix=C,general_desc=A(national_number_pattern='0\\d|1\\d{2,6}|8\\d{3,4}',possible_number_pattern=D),toll_free=A(national_number_pattern='116(?:000|111)',possible_number_pattern='\\d{6}',example_number='116000'),premium_rate=A(national_number_pattern='1180|8(?:2\\d{3}|[89]\\d{2})',possible_number_pattern='\\d{4,5}'),emergency=A(national_number_pattern='0[123]|11[023]',possible_number_pattern='\\d{2,3}',example_number=E),short_code=A(national_number_pattern='0[1-4]|1(?:1(?:[02-4]|6(?:000|111)|8[0189])|55|655|77)|821[57]4',possible_number_pattern=D,example_number=E),standard_rate=A(national_number_pattern=F,possible_number_pattern=G,example_number=F),carrier_specific=A(national_number_pattern='16\\d{2}',possible_number_pattern=G,example_number='1655'),short_data=True)