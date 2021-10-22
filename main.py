import json

path = "./user.json"


with open(path) as reader:
    data = reader.read()

user = json.loads(data)
print(type(user))