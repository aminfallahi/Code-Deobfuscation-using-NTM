'Auto-generated file, do not edit by hand. CI metadata'
C='\\d{8}'
A='NA'
from ..phonemetadata import NumberFormat as D,PhoneNumberDesc as B,PhoneMetadata as E
F=E(id='CI',country_code=225,international_prefix='00',general_desc=B(national_number_pattern='[02-8]\\d{7}',possible_number_pattern=C),fixed_line=B(national_number_pattern='(?:2(?:0[023]|1[02357]|[23][045]|4[03-5])|3(?:0[06]|1[069]|[2-4][07]|5[09]|6[08]))\\d{5}',possible_number_pattern=C,example_number='21234567'),mobile=B(national_number_pattern='(?:0[1-9]|4\\d|5[14-9]|6[015-79]|7[578]|87)\\d{6}',possible_number_pattern=C,example_number='01234567'),toll_free=B(national_number_pattern=A,possible_number_pattern=A),premium_rate=B(national_number_pattern=A,possible_number_pattern=A),shared_cost=B(national_number_pattern=A,possible_number_pattern=A),personal_number=B(national_number_pattern=A,possible_number_pattern=A),voip=B(national_number_pattern=A,possible_number_pattern=A),pager=B(national_number_pattern=A,possible_number_pattern=A),uan=B(national_number_pattern=A,possible_number_pattern=A),voicemail=B(national_number_pattern=A,possible_number_pattern=A),no_international_dialling=B(national_number_pattern=A,possible_number_pattern=A),number_format=[D(pattern='(\\d{2})(\\d{2})(\\d{2})(\\d{2})',format='\\1 \\2 \\3 \\4')],leading_zero_possible=True)