vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
for letter in word: #берем каждую букву в слове
    if letter in vowels: #и если она содержиться в списке гласных
        print(letter) # отображаем эту букву на экране