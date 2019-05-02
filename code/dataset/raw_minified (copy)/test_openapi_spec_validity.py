import json
from jsonschema import RefResolver as A
from swagger_spec_validator import validator20 as B
def C(flask_app_client):C=flask_app_client.get('/api/v1/swagger.json').data;D=json.loads(C.decode('utf-8'));assert isinstance(B.validate_spec(D),A)