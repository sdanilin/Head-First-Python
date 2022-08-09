'''Create def'''

# def search4vowels():
#     """Выводит гласные, найденные в введенном слове."""
#     vowels = set('aeiou')
#     word = input("provide a world to search for vowels:")  # сообщает интерпритатору о необходимости запросить у пользователя строку для поиска глассных (выводит поле для воода слова, в котором будеит производиться поиск гласных)
#     found = vowels.intersection(set(word))  # intersection сообщил нам, что в переменной word содержаться глассные. Множество i включает все объекты их vowels7 которые так же присутствуют в set(word)
#     for vowel in found:
#         print(vowel)
# print(search4vowels())

#Булевые значения
# """Если объект равен 0, он всегда False"""
# print(bool(0))
# print(bool(0.0))
#
# """Пустоя строка, пустой список и пустой словарь оцениваются как False"""
# print(bool(''))
# print(bool([]))
# print(bool({}))
#
# """Значение None в Python всегда False"""
# print(bool(None))
#
# """Ненулевые числа всегда True, даже отрицательные"""
# print(bool(1))
# print(bool(-1))
# print(bool(42))
# print(bool(0.000000000000000000000000000001))
#
# """Непустая строка всегда True"""
# print(bool('Panic'))
#
# """Непустая встроенная структура данных всегда True"""
# print(bool([42, 43, 44]))
# print(bool({'a':42, 'b':42}))


def search4vowels(word):
    """Выводит гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))  # intersection сообщил нам, что в переменной word содержаться глассные. Множество i включает все объекты их vowels7 которые так же присутствуют в set(word)
    return bool(found) #вызов функции bool и передача имени структуры данных, которая содержит результат поиска гласных
print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))
print(search4vowels('sky'))