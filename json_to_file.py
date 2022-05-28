import json

friends = [
    {'name': 'Max', 'age': '20', 'phones': [123, 456]},
    {'name': 'Leo', 'age': '23'}
    ]

print(type(friends))

with open('friends.jon', 'w') as f:
    json_friends = json.dump(friends, f)

with open('friends.jon', 'r') as f:
    friends = json.load(f)

print((friends))
print(type(friends))

