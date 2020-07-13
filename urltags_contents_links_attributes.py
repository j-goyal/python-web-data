import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter url- ')
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('span')
print(tags)

sum=0
for i in tags:
    sum=sum+int(i.contents[0])   #print(i) {TAGS} , print(i.attrs) {ATTRIBUTES}, print(i.get('href',None)) {URL}

print(sum)

"""print('\n\n')

for i in tags:
    print(i.get('href',None))
"""