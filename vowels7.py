vowels = ['a', 'e', 'i', 'o', 'u']
word = input("provide a world to search for vowels:") #сообщает интерпритатору о необходимости запросить у пользователя строку для поиска глассных (выводит поле для воода слова, в котором будеит производиться поиск гласных)
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)