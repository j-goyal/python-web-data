import json


#LIST OF DICTIONARIES or DICTIONARIES are used as data
data = '''       
[
  { "id" : "001",
    "x" : "2",
    "name" : "Chuck"
  } ,
  { "id" : "009",
    "x" : "7",
    "name" : "Brent"
  }
]
'''

info = json.loads(data)      #Returns LIST of DICTIONARIES
print('User count:', len(info))
#print(type(info))

for item in info:                #iterate over the list
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'])