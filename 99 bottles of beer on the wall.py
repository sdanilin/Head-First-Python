#add "bottles" to new varuable with name "word"
word = "bottles"
for beer_num in range(99, 0, -1): #для переменной beer_num задаётся цикл повтора в диапазоне с шагом -1
    print(beer_num, word, "of beer on the wall.") #написать первый номер цикла, слово "bottles", "of beer on the wall."
    print(beer_num, word, "of beer.") #"99 bottles of beer."
    print("Take one down.") # ""Take one down.""
    print("Pass it around.") #"Pass it around."
    if beer_num == 1: #если номер бутылки из цикла равен 1
        print("No more bottles of beer on the wall.") # если да то написать "No more bottles of beer on the wall."
    else: #еще/иначе
        new_num = beer_num - 1 #запомнить кол-во бутылок пива для селдующей итерации в другой переменной
        if new_num == 1: #если новая переменная равна 1 (если собираемся выпить последнюю будтылку)
            word = "bottle" #то значение переменной меняется на бутылка
        print(new_num, word, "of beer on the wall.") # 1 bottle of beer on the wall(завершаем слова песни для итерации)
    print() #выполнить цикл (в конце итерации печатаем пустую строку. Если все итерации завершены завершаем программу)