from selenium import webdriver as B
from SenseCells.tts import tts
def A(proxy_username,proxy_password):tts('Connecting to proxy server.');A=B.Firefox();A.get('http://10.1.1.9:8090/httpclient.html');C=A.find_element_by_name('username');D=A.find_element_by_name('password');C.send_keys(proxy_username);D.send_keys(proxy_password);A.find_element_by_name('btnSubmit').click()