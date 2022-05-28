# Analog #1
with open('bytes.txt', 'wb') as f:
    str = 'Привет мир'
    f.write(str.encode('utf-8'))

# Analog #2
with open('bytes.txt', 'w', encoding='utf-8') as f:
    f.write('Привет мир')


with open('bytes.txt', 'rb') as f:
    result = f.read()
    print(result)
    print(type(result))
    # Декодируем для нормального вывода
    s = result.decode('utf-8')
    print(s)

