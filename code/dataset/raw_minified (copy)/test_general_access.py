C='/api/v1/users/1'
A='GET'
import pytest as B
@B.mark.parametrize('http_method,http_path',((A,'/api/v1/users/'),(A,C),('PATCH',C),(A,'/api/v1/users/me')))
def D(http_method,http_path,flask_app_client):A=flask_app_client.open(method=http_method,path=http_path);assert A.status_code==401