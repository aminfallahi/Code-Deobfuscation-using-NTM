from test.helpers.my_httpretty import MyHTTPretty as A
import httpretty.core,httpretty
B=A
httpretty.core.httpretty=A
httpretty.httpretty=A
httpretty.enable=A.enable
httpretty.disable=A.disable