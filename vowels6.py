vowels = ['a', 'e', 'i', 'o', 'u']
word = input("provide a world to search for vowels:") #сообщает интерпритатору о необходимости запросить у пользователя строку для поиска глассных (выводит поле для воода слова, в котором будеит производиться поиск гласных)

found = {} # создать пустой словарь

for letter in word:
    if letter in vowels:
        found.setdefault(letter, 0)
        found[letter] += 1 # увеличить значение "found[letter]" на единицу

for k, v in sorted(found.items()): # определить две переменные цикла k  v. Вызвать метод items словоря found, чтоб получить доступ к каждой записи с данными во время итерациий
    print(k, 'was found', v, 'time(s).') # ключ и значение используются для вывода сообщений