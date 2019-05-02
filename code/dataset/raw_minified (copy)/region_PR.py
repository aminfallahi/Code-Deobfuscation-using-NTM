'Auto-generated file, do not edit by hand. PR metadata'
H='1'
G='7872345678'
F='(?:787|939)[2-9]\\d{6}'
D='\\d{10}'
C='\\d{7}(?:\\d{3})?'
B='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as E
I=E(id='PR',country_code=1,international_prefix='011',general_desc=A(national_number_pattern='[5789]\\d{9}',possible_number_pattern=C),fixed_line=A(national_number_pattern=F,possible_number_pattern=C,example_number=G),mobile=A(national_number_pattern=F,possible_number_pattern=C,example_number=G),toll_free=A(national_number_pattern='8(?:00|44|55|66|77|88)[2-9]\\d{6}',possible_number_pattern=D,example_number='8002345678'),premium_rate=A(national_number_pattern='900[2-9]\\d{6}',possible_number_pattern=D,example_number='9002345678'),shared_cost=A(national_number_pattern=B,possible_number_pattern=B),personal_number=A(national_number_pattern='5(?:00|33|44|66|77|88)[2-9]\\d{6}',possible_number_pattern=D,example_number='5002345678'),voip=A(national_number_pattern=B,possible_number_pattern=B),pager=A(national_number_pattern=B,possible_number_pattern=B),uan=A(national_number_pattern=B,possible_number_pattern=B),voicemail=A(national_number_pattern=B,possible_number_pattern=B),no_international_dialling=A(national_number_pattern=B,possible_number_pattern=B),national_prefix=H,national_prefix_for_parsing=H,leading_digits='787|939')