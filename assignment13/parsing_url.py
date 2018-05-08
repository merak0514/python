# From https://www.py4e.com/html3/13-web
import xml.etree.ElementTree as ET
data = '''
<person>
    <name>dasf</name>
    <phone type="stupid">
        <phone2 type="stupid">
            132131
        </phone2>
    </phone>
</person>
'''

tree = ET.fromstring(data)
print('name:', tree.find('name').text)
print('person:', tree.find('phone').find('phone2').get('type'))
