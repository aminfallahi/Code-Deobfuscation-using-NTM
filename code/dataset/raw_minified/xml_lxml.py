import lxml.etree,lxml
from lxml import etree
from defusedxml.lxml import fromstring as B
from defuxedxml import lxml as D
A="<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"
C=lxml.etree.fromstring(A)
C=B(A)