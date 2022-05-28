import json

friends = [
    {'name': 'Max', 'age': '20', 'phones': [123, 456]},
    {'name': 'Leo', 'age': '23'}
    ]

print(type(friends))

json_friends = json.dumps(friends)

print(json_friends)
print(type(json_friends))

friends = json.loads(json_friends)
print(friends)
print(type(friends))


