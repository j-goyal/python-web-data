'''In this assignment you will write a Python program .The program will
 prompt for a URL, read the JSON data from that URL using urllib and then
  parse and extract the comment counts from the JSON data, compute the
  sum of the numbers in the file and enter the sum below:
'''

import json
import urllib.request as ur

hand=ur.urlopen('http://py4e-data.dr-chuck.net/comments_246128.json')
data=hand.read().decode()

print(data)
dic=json.loads(data)

lst=dic['comments']

print(lst)

suma=0
for i in lst:
    suma=suma+i['count']

print(suma)