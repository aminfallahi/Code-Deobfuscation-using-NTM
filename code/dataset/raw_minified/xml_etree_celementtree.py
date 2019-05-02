G=print
D='filethatdoesntexist.xml'
import xml.etree.cElementTree as A,defusedxml.cElementTree as B
E="<note>\n<to>Tove</to>\n<from>Jani</from>\n<heading>Reminder</heading>\n<body>Don't forget me this weekend!</body>\n</note>"
C=A.fromstring(E)
G(C)
A.parse(D)
A.iterparse(D)
F=A.XMLParser()
C=B.fromstring(E)
G(C)
B.parse(D)
B.iterparse(D)
F=B.XMLParser()