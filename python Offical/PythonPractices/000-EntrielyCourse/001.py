import urllib.request
u = urllib.request.urlopen('https://ctabustracker.com/home?stop=14791&route=22')

from xml.etree.ElementTree import parse

doc = parse(u)

print(doc)

for pt in doc.findall(".//pt"):
    print(pt.text)

