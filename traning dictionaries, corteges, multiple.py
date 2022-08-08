# '''Dictionaries'''
#
# person3 = { 'Name': 'Ford Prefect',
#             'Gender': 'Male',
#             'Occupation': 'Researcher',
#             'Home Planet': 'Betelgeuse Seven' }
# person3['Age'] = 33 # добавлено в словарь
# print(person3)
# print(person3['Home Planet'])
# print(person3['Name'])
#
#
# # Счетчик частоты
# found = {}
# print(found)
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0
# print(found)
# found['e'] = found['e'] + 1 # счетчик частоты (увеличиваем счетчик ассоциированный с ключом 'e')
# print(found)
# found['e'] += 1 # увеличение счетчика 'e' еще раз
# print(found)
#
# # Итерации по ключам и значениям в словаре
# for k in sorted(found): # sorted сортирует вывовод в алафавитном порядке
#     print(k, 'was found', found[k], 'time(s).')
#
# # Итерации по словарям с использованием items - возвращает список пар ключ/занчение
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'time(s).')
#
# # Предотвращение ошибок KeyError во время выполения
# # fruits = {}
# # fruits['apples'] = 10
# # print(fruits)
# # print('apples' in fruits) # значение связано с ключомб и при использовании оператора in для проверки существования ключа никакие ошибки не появились
# fruits = {}
# fruits['apples'] = 10
# print(fruits)
# print('apples' in fruits) # значение связано с ключомб и при использовании оператора in для проверки существования ключа никакие ошибки не появились
# if 'babanans' in fruits: # проверяем присутствие ключа bananas в словаре и если он отсутсвует, инициируем занчением 1
#     fruits['bananas'] += 1 # предотвращаем KeyError
# else:
#     fruits['bananas'] = 1
# print(fruits)
# if 'pears' not in fruits:
#     fruits['pears'] = 0
# fruits['pears'] += 1
# print(fruits)
# if 'pears' not in fruits:
#     fruits['pears'] = 0
# fruits['pears'] += 1
# print(fruits)
# fruits.setdefault('pears', 0) # единственный вызов setdefault позволит заменить двухстрочную иструкцию if/not in
# fruits['pears'] += 1
# print(fruits)

'''Multiple'''

# vowels = {'a', 'e', 'e', 'i', 'o', 'u', 'u'} #мнодества определяются фигурными скобками
# print(vowels)
#
# vowels2 = set('aeeiouu') # создать множество передав функции set последовательность (например строку)
# print(vowels2)

# #union
# vowels = set('aeiou')
# word = 'hello'
# u = vowels.union(set(word)) #метод union объединяет два множества, а результат объединения присваивается новой переменной 'u'. Python конвертирует значение переменной word в множество объектов-символов (попутно удаляя все повторения)
# u_list = sorted(list(u)) #отсортированный список букв без повторений
#
# #difference
# d = vowels.difference(set(word)) # difference сравнивает объекты из множества vowels с объектами из множества set(word), затем возвращает новое множество объектов d, которые содержаться в vowels и не содержаться в set(word)
#
# #intersecton
# i = vowels.intersection(set(word)) # intersection сообщил нам, что в переменной word содержаться глассные e и o. Множество i включает все объекты их vowelsб которые так же присутствуют в set(word)


'''tuple (кортеж)'''

# vowels = ['a', 'e', 'i', 'o', 'u']
# type(vowels) # встроенная функция type помогает узнать тип любого созданного объекта
# print(type(vowels))
# vowels2 = ('a', 'e', 'i', 'o', 'u')
# type(vowels2)
# print(type(vowels2)) #круглые скобки показывает, что это кортеж

# vowels[2] = 'I' #изменился объект списка с индексом 2
# print(vowels)

# vowels2[2] = 'I' #ничего не изменилось, потому что кортежы неизменяемы
# print(vowels2) # если данные в вашей структуре никогда не меняются, положите их в кортеж

# t2 = ('Python',)
# type('t2')
# print(type(t2))
# print(t2)


'''Хранение данных в таблицах'''

#Словарь Словарей
people = {} # создадим новый пустой словарь
people['Ford'] = { 'Name': 'Ford Prefect', #ключ Ford, а значение другой словарь
              'Gender': 'Male',
              'Occupation': 'Researcher',
              'Home Planet': 'Betelgeuse Seven' }

people['Artur'] = { 'Name': 'Artur Dent',
              'Gender': 'Male',
              'Occupation': 'Sendwich-Maker',
              'Home Planet': 'Earth' }

people['Trillian'] = { 'Name': 'Tricia McMillan',
              'Gender': 'Female',
              'Occupation': 'Mathematician',
              'Home Planet': 'Earth' }

people['Robot'] = { 'Name': 'Marvin',
              'Gender': 'Unknown',
              'Occupation': 'Paranoid Android',
              'Home Planet': 'Unknown' }
print(people)
import pprint #модуль который принимает любую структуру данных и вывадит ее в удобном для чтения формате
pprint.pprint(people)