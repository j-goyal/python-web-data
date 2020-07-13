import xml.etree.ElementTree as ET

data = '''
<stuff>
  <users>
    <user x="2">
      <id>001</id>
      <name>Chuck</name>
    </user>
    <user x="7">
      <id>009</id>
      <name>Brent</name>
    </user>
  </users>
</stuff>'''

parse = ET.fromstring(data)     #RETURN PARENT TAG

lst = parse.findall('users/user')   # WE CAN ALSO WRITE THIS './/user'
print(lst)
#print('User count:', len(lst))

for item in lst:
    print('Name', item.find('name').text)
    print('Id', item.find('id').text)
    print('Attribute', item.get('x'))