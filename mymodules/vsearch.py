def search4vowels(phrase:str) -> set: #в аннотации указали, что в аргументе word ожидается строка. Указали, что функция возвращает множество
    """Возвращает, гласные, найденные в указанном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))  #возврат данных без использования переменной found


def search4letters(phrase:str, letters:str='aeiou') -> set: #make 'letters' default
    """Возвращает множество букв из latters, найденных в указанной фразе"""
    return set(letters).intersection(set(phrase)) #создаем объект множества из letters. найдем пересечение множества, созданного из letters с множеством созданным из phrase. И возвращаем результат вызывающему коду.

# print(help(search4vowels)) #функция help отображает не только аннотации, но и строку документации
# print(search4vowels('hitch-hiker'))
# print(search4vowels('galaxy'))
# print(search4vowels('sky'))
#
# print(help(search4letters))
# print(search4letters('hitch-hiker', 'aeiou'))
# print(search4letters('galaxy', 'xyz'))
# print(search4letters('life, the universe, and everything', 'o'))

print(search4letters('life, the universe, and everything'))
print(search4letters('life, the universe, and everything', 'aeiou'))
# print(search4vowels('life, the universe, and everything'))
print(search4letters(letters='xyz', phrase='galaxy')) #порядок аргументов не важен если присваивать их по именам параметров