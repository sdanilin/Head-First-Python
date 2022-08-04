vowels = set('aeiou')
word = input("provide a world to search for vowels:") #сообщает интерпритатору о необходимости запросить у пользователя строку для поиска глассных (выводит поле для воода слова, в котором будеит производиться поиск гласных)
# i = vowels.intersection(set(word))
# print(i)
found = vowels.intersection(set(word))
for vowel in found:
    print(vowel)