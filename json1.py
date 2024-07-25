import json

data = '''
{
    "name" : "Sriansh" ,
    "phone" : "intl",
    "number" : "+91 88 511 2848",
    "email" : {
        "hide": "yes"
    }
}'''

info = json.loads(data)
print("Name:", info["name"])
print("Hide:", info["email"]["hide"])