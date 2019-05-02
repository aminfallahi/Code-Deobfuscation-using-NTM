from smsapi.client import SmsAPI as C
A=C()
A.set_username('client_username')
A.set_password('client_password')
A.service('sms').action('send')
A.set_content('sample message')
A.set_to('some_phone_number')
D=A.execute()
for B in D:print(B.id,B.points,B.status)