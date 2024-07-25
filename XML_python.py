import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Sriansh</name>
    <phone type="intl">
        +91 828 7574 90
    </phone>
    <email hide="yes" />
</person>'''

tree =ET.fromstring(data)
print('Name', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))