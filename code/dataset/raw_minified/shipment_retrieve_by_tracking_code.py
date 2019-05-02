C=print
import easypost as B
B.api_key='cueqNZUb3ldeWTNX7MU3Mel8UXtaAMUi'
A=B.Shipment.retrieve('LN123456789US')
C(A.id)
A.refresh()
C(A.id)
C(A.label(file_format='PDF'))