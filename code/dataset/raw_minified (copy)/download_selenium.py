' Download the selenium server jar file '
import os
from seleniumbase.core import selenium_launcher as A
if not A.is_available_locally():A.download_selenium()
for B in os.listdir('.'):
	if B.startswith('selenium-server-standalone-'):os.rename(B,'selenium-server-standalone.jar')