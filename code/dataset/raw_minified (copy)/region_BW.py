'Auto-generated file, do not edit by hand. BW metadata'
G='\\1 \\2'
F='\\d{8}'
E='\\d{7}'
A='NA'
from ..phonemetadata import NumberFormat as C,PhoneNumberDesc as B,PhoneMetadata as D
H=D(id='BW',country_code=267,international_prefix='00',general_desc=B(national_number_pattern='[2-79]\\d{6,7}',possible_number_pattern='\\d{7,8}'),fixed_line=B(national_number_pattern='(?:2(?:4[0-48]|6[0-24]|9[0578])|3(?:1[0235-9]|55|[69]\\d|7[01])|4(?:6[03]|7[1267]|9[0-5])|5(?:3[0389]|4[0489]|7[1-47]|88|9[0-49])|6(?:2[1-35]|5[149]|8[067]))\\d{4}',possible_number_pattern=E,example_number='2401234'),mobile=B(national_number_pattern='7(?:[1-6]\\d|7[014-8])\\d{5}',possible_number_pattern=F,example_number='71123456'),toll_free=B(national_number_pattern=A,possible_number_pattern=A),premium_rate=B(national_number_pattern='90\\d{5}',possible_number_pattern=E,example_number='9012345'),shared_cost=B(national_number_pattern=A,possible_number_pattern=A),personal_number=B(national_number_pattern=A,possible_number_pattern=A),voip=B(national_number_pattern='79[12][01]\\d{4}',possible_number_pattern=F,example_number='79101234'),pager=B(national_number_pattern=A,possible_number_pattern=A),uan=B(national_number_pattern=A,possible_number_pattern=A),voicemail=B(national_number_pattern=A,possible_number_pattern=A),no_international_dialling=B(national_number_pattern=A,possible_number_pattern=A),number_format=[C(pattern='(\\d{3})(\\d{4})',format=G,leading_digits_pattern=['[2-6]']),C(pattern='(7\\d)(\\d{3})(\\d{3})',format='\\1 \\2 \\3',leading_digits_pattern=['7']),C(pattern='(90)(\\d{5})',format=G,leading_digits_pattern=['9'])])