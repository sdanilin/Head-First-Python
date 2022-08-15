def search4vowels(phrase:str) -> set: #в аннотации указали, что в аргументе word ожидается строка. Указали, что функция возвращает множество
    """Возвращает, гласные, найденные в указанном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))  #возврат данных без использования переменной found


def search4letters(phrase:str, letters:str) -> set:
    return set(letters).intersection(set(phrase)) #создаем объект множества из letters. найдем пересечение множества, созданного из letters с множеством созданным из phrase. И возвращаем результат вызывающему коду.

print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))
print(search4vowels('sky'))
print(help(search4vowels)) #функция help отображает не только аннотации, но и строку документации