#READ URL FROM WEB CONTAINING XML DATA AND...
#FIND SUM UNDER 'COUNT' TAG


import urllib.request as ur, urllib.parse as up, urllib.error as ue
import xml.etree.ElementTree as ET

hand = ur.urlopen('http://py4e-data.dr-chuck.net/comments_246127.xml')
data = hand.read()

tree = ET.fromstring(data)

counts=tree.findall('.//count')

suml = 0
for count in counts:
    suml += int(count.text)

print(suml)