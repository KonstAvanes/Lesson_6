import json
import pickle


my_fav_group = {'name': 'Aqua', 'Track': ['Roses and red', 'Barbie girl'],
                'album': [{'name': 'Aquarium', 'year': 1997}, {'name': 'Aquarius', 'year': 2000}]}

print(my_fav_group)

j_group = json.dumps(my_fav_group)
print(j_group)

p_group = pickle.dumps(my_fav_group)
print(p_group)

with open('group.json', 'w', encoding='utf-8') as f:
    json.dump(my_fav_group, f)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_fav_group, f)
