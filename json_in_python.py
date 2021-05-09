import json
person = {
    'name':'John',
    'age': 30,
    'has_children': False,
}

personJSN = json.dumps(person,indent=1)
print(personJSN)

with open('person.json','w') as file:
    json.dump(person,file,indent=1)

pr = json.loads(personJSN)
print(pr)