import pickle

person = {'name': 'Max', 'phones': [123, 345]}

with open('person.dat', 'wb') as f:
    pickle.dump(person, f)

print('Object input')

with open('person.dat', 'rb') as f:
    person = pickle.load(f)

print(person)
