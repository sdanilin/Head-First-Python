def search4vowels(word:str) -> set: #в аннотации указали, что в аргументе word ожидается строка. Указали, что функция возвращает множество
    """Возвращает, гласные, найденные в указанном слове"""
    vowels = set('aeiou')
    return vowels.intersection(set(word))  #возврат данных без использования переменной found
print(search4vowels('hitch-hiker'))
print(search4vowels('galaxy'))
print(search4vowels('sky'))
print(help(search4vowels)) #функция help отображает не только аннотации, но и строку документации