vowels = set('aeiou')
word = input("provide a world to search for vowels:") #сообщает интерпритатору о необходимости запросить у пользователя строку для поиска глассных (выводит поле для воода слова, в котором будеит производиться поиск гласных)
# i = vowels.intersection(set(word))
# print(i)
found = vowels.intersection(set(word)) # intersection сообщил нам, что в переменной word содержаться глассные. Множество i включает все объекты их vowels7 которые так же присутствуют в set(word)
for vowel in found:
    print(vowel)