'Auto-generated file, do not edit by hand. CH metadata'
E='\\d{3,4}'
D=None
B='\\d{3,6}'
from ..phonemetadata import NumberFormat,PhoneNumberDesc as A,PhoneMetadata as C
F=C(id='CH',country_code=D,international_prefix=D,general_desc=A(national_number_pattern='[1-9]\\d{2,5}',possible_number_pattern=B),toll_free=A(national_number_pattern='1(?:16\\d{3}|47)|5200',possible_number_pattern=B,example_number='116000'),premium_rate=A(national_number_pattern='1(?:145|8\\d{2})|543|83111',possible_number_pattern='\\d{3,5}',example_number='543'),emergency=A(national_number_pattern='1(?:1[278]|44)',possible_number_pattern='\\d{3}',example_number='112'),short_code=A(national_number_pattern='1(?:0[78]\\d{2}|1(?:[278]|45|6(?:000|111))|4(?:[03457]|1[45])|6(?:00|[1-46])|8(?:02|1[189]|50|7|8[08]|99))|[2-9]\\d{2,4}',possible_number_pattern=B,example_number='147'),standard_rate=A(national_number_pattern='1(?:4(?:[035]|1\\d)|6\\d{1,2})',possible_number_pattern=E,example_number='1600'),carrier_specific=A(national_number_pattern='5(?:200|35)',possible_number_pattern=E,example_number='535'),short_data=True)