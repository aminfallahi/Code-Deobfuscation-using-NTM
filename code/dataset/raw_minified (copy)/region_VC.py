'Auto-generated file, do not edit by hand. VC metadata'
F='1'
E='\\d{7}(?:\\d{3})?'
C='\\d{10}'
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as D
G=D(id='VC',country_code=1,international_prefix='011',general_desc=A(national_number_pattern='[5789]\\d{9}',possible_number_pattern=E),fixed_line=A(national_number_pattern='784(?:266|3(?:6[6-9]|7\\d|8[0-24-6])|4(?:38|5[0-36-8]|8[0-8])|5(?:55|7[0-2]|93)|638|784)\\d{4}',possible_number_pattern=E,example_number='7842661234'),mobile=A(national_number_pattern='784(?:4(?:3[0-4]|5[45]|89|9[0-58])|5(?:2[6-9]|3[0-4]))\\d{4}',possible_number_pattern=C,example_number='7844301234'),toll_free=A(national_number_pattern='8(?:00|44|55|66|77|88)[2-9]\\d{6}',possible_number_pattern=C,example_number='8002345678'),premium_rate=A(national_number_pattern='900[2-9]\\d{6}',possible_number_pattern=C,example_number='9002345678'),shared_cost=A(national_number_pattern=B,possible_number_pattern=B),personal_number=A(national_number_pattern='5(?:00|33|44|66|77|88)[2-9]\\d{6}',possible_number_pattern=C,example_number='5002345678'),voip=A(national_number_pattern=B,possible_number_pattern=B),pager=A(national_number_pattern=B,possible_number_pattern=B),uan=A(national_number_pattern=B,possible_number_pattern=B),voicemail=A(national_number_pattern=B,possible_number_pattern=B),no_international_dialling=A(national_number_pattern=B,possible_number_pattern=B),national_prefix=F,national_prefix_for_parsing=F,leading_digits='784')