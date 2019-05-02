'Auto-generated file, do not edit by hand. NC metadata'
F='1000'
E='\\d{2,4}'
D=None
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as C
G=C(id='NC',country_code=D,international_prefix=D,general_desc=A(national_number_pattern='1\\d{1,3}|3\\d{3}|5\\d{2}',possible_number_pattern=E),toll_free=A(national_number_pattern='10(?:00|1[23]|3[0-2]|88)|3631|577',possible_number_pattern='\\d{3,4}',example_number=F),premium_rate=A(national_number_pattern=B,possible_number_pattern=B),emergency=A(national_number_pattern='1[5-8]',possible_number_pattern='\\d{2}',example_number='15'),short_code=A(national_number_pattern='1(?:0(?:0[06]|1[02-46]|20|3[0125]|42|5[058]|77|88)|[5-8])|3631|5[6-8]\\d',possible_number_pattern=E,example_number=F),standard_rate=A(national_number_pattern='5(?:67|88)',possible_number_pattern='\\d{3}',example_number='567'),carrier_specific=A(national_number_pattern=B,possible_number_pattern=B),short_data=True)