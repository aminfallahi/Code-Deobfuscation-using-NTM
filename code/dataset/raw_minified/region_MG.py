'Auto-generated file, do not edit by hand. MG metadata'
G='0'
F='\\d{9}'
E='\\d{7,9}'
A='NA'
from ..phonemetadata import NumberFormat as C,PhoneNumberDesc as B,PhoneMetadata as D
H=D(id='MG',country_code=261,international_prefix='00',general_desc=B(national_number_pattern='[23]\\d{8}',possible_number_pattern=E),fixed_line=B(national_number_pattern='20(?:2\\d{2}|4[47]\\d|5[3467]\\d|6[279]\\d|7(?:2[29]|[35]\\d)|8[268]\\d|9[245]\\d)\\d{4}',possible_number_pattern=E,example_number='202123456'),mobile=B(national_number_pattern='3[2-49]\\d{7}',possible_number_pattern=F,example_number='321234567'),toll_free=B(national_number_pattern=A,possible_number_pattern=A),premium_rate=B(national_number_pattern=A,possible_number_pattern=A),shared_cost=B(national_number_pattern=A,possible_number_pattern=A),personal_number=B(national_number_pattern=A,possible_number_pattern=A),voip=B(national_number_pattern='22\\d{7}',possible_number_pattern=F,example_number='221234567'),pager=B(national_number_pattern=A,possible_number_pattern=A),uan=B(national_number_pattern=A,possible_number_pattern=A),voicemail=B(national_number_pattern=A,possible_number_pattern=A),no_international_dialling=B(national_number_pattern=A,possible_number_pattern=A),national_prefix=G,national_prefix_for_parsing=G,number_format=[C(pattern='([23]\\d)(\\d{2})(\\d{3})(\\d{2})',format='\\1 \\2 \\3 \\4',national_prefix_formatting_rule='0\\1')])