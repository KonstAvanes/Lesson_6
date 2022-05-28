person = {'name': 'Max', 'phones': [123, 345]}

# Откроем файл
with open('person.dat', 'wb') as f:
    # Запишем объект в фал построчно
    # Сначала возьмем имя
    name = person['name']
    # Добавим перенос строки, переведем в байты и запишем в файл
    f.write(f'{name}\n'.encode('utf-8'))
    # Получим телефоны
    phones = person['phones']
    # Запишем 1 телефон в новую строку
    for phone in phones:
        f.write(f'{phone}\n'.encode('utf-8'))

print('Object input')
