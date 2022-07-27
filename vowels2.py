vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
found = [] #creat empty list
for letter in word:
    if letter in vowels:
        #добавляем код, определяющий необходимость включения буквы в список найденных гласных
        if letter not in found:
            found.append(letter)
#когда заканчивается первый цикл for начинает выполняться второй который отображает найденные в слове гласные
for vowel in found:
    print(vowels)