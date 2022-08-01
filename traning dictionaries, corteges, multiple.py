'''Dictionaries'''

person3 = { 'Name': 'Ford Prefect',
            'Gender': 'Male',
            'Occupation': 'Researcher',
            'Home Planet': 'Betelgeuse Seven' }
person3['Age'] = 33 # добавлено в словарь
print(person3)
print(person3['Home Planet'])
print(person3['Name'])


# Счетчик частоты
found = {}
print(found)
found['a'] = 0
found['e'] = 0
found['i'] = 0
found['o'] = 0
found['u'] = 0
print(found)
found['e'] = found['e'] + 1 # счетчик частоты (увеличиваем счетчик ассоциированный с ключом 'e')
print(found)
found['e'] += 1 # увеличение счетчика 'e' еще раз
print(found)

# Итерации по ключам и значениям в словаре
for k in sorted(found): # sorted сортирует вывовод в алафавитном порядке
    print(k, 'was found', found[k], 'time(s).')

# Итерации по словарям с использованием items - возвращает список пар ключ/занчение
for k, v in sorted(found.items()):
    print(k, 'was found', v, 'time(s).')