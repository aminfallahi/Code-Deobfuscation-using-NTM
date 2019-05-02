import pywapi as B
from SenseCells.tts import tts
def A(city_name,city_code):D='current_conditions';A=B.get_weather_from_weather_com(city_code);C='Weather.com says: It is '+A[D]['text'].lower()+' and '+A[D]['temperature']+'degree celcius now in '+city_name;tts(C)