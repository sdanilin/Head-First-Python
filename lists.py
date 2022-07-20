# prices = []
# temps = [32.0, 212.0, 0.0, 81.6, 100.0, 45.3]
# words = ["hello", "world"]
# car_ditails = ["Tpyota", "RAV4", 2.2, 60807]
#
# #list of odject_lists
# everything = [prices, temps, words, car_ditails]
# #заполнение списка при объявлении
# odds_and_ends = [ [1, 2, 3], ["a", "b", "c"], ["one", "two", "three"] ]

vowels = ['a', 'e', 'i', 'o', 'u']
word = "Milliways"
for letter in word: #берем каждую букву в слове
    if letter in vowels: #и если она содержиться в списке гласных
        print(letter) # отображаем эту букву на экране

# #The experiments
# found = [] #empty list
# len(found) #proof that list don't have any objects
#
# found.append('a') #добавляем букву в существующий список с помощью метода "append"
# found.append('e')
# found.append('i')
# found.append('o')
# len(found) #функция для определения кол-ва объектов в коллекции
# found #вызываем список на экран