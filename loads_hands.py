# Читаем объект из файла
# Откроем файл
with open('person.dat', 'rb') as f:
    # Теперь нам надо знать как записали данные
    # Прочитаем файл в список
    result = f.readlines()

# Теперь воссоздаем исходный объект
person = {}
# Первый элемент это имя
person['name'] = result[0].decode('utf--8').replace('\n', '')
# Далее идут телефоны
phones = []

for bphone in result[1:]:
    phones.append(bphone.decode('utf-8').replace('\n', ''))
person['phones'] = phones
# Очень сложно, если что-то измениться, никогда не восстановим
print(person)