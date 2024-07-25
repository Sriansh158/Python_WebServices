import json

input = '''
[
    {  
         "id" : "001",
        "x" : "1",
        "name" : "Sriansh"
    },
    {   
        "id" : "007",
        "x" : "7",
        "name" : "Vansh"
    }
]'''

info = json.loads(input)
print("User Count :", len(info))

for item in info:
    print("Name :",item['name'])
    print("ID :",item['id'])
    print("Attributes :",item['x'])