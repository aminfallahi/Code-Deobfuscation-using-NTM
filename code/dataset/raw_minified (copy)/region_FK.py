'Auto-generated file, do not edit by hand. FK metadata'
C='\\d{5}'
A='NA'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as B,PhoneMetadata as D
E=D(id='FK',country_code=500,international_prefix='00',general_desc=B(national_number_pattern='[2-7]\\d{4}',possible_number_pattern=C),fixed_line=B(national_number_pattern='[2-47]\\d{4}',possible_number_pattern=C,example_number='31234'),mobile=B(national_number_pattern='[56]\\d{4}',possible_number_pattern=C,example_number='51234'),toll_free=B(national_number_pattern=A,possible_number_pattern=A),premium_rate=B(national_number_pattern=A,possible_number_pattern=A),shared_cost=B(national_number_pattern=A,possible_number_pattern=A),personal_number=B(national_number_pattern=A,possible_number_pattern=A),voip=B(national_number_pattern=A,possible_number_pattern=A),pager=B(national_number_pattern=A,possible_number_pattern=A),uan=B(national_number_pattern=A,possible_number_pattern=A),voicemail=B(national_number_pattern=A,possible_number_pattern=A),no_international_dialling=B(national_number_pattern=A,possible_number_pattern=A))