def search4vowels(word):
    """Выводит гласные, найденные в указанном слове."""
    vowels = set('aeiou')
    found = vowels.intersection(set(word))  # intersection сообщил нам, что в переменной word содержаться глассные. Множество i включает все объекты их vowels7 которые так же присутствуют в set(word)
    for vowel in found:
        print(vowel)
print(search4vowels('hitch-hiker'))