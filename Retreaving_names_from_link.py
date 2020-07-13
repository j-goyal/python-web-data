import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url=input('Enter url- ')   # http://py4e-data.dr-chuck.net/known_by_Rayhan.html
html=urllib.request.urlopen(url).read()
soup=BeautifulSoup(html, 'html.parser')

tags=soup('a')
pos=18
count=7
for i in range(count):
    new_link=tags[pos-1].get('href',None)
    print(tags[pos-1].contents[0])
    html = urllib.request.urlopen(new_link).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')


