phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
for i in range(4): #этот цикл извлекает последние четыре объекта из "plisy", удаляя из из строки "nic!"
        plist.pop()
plist.pop(0) #извлечем первую букву списка ('D')
plist.remove("'") #находим и удаляем апостроф
plist.extend([plist.pop(), plist.pop()]) #поменяем местами два объекта в конце списка, предварительно вынув каждый объект из списка,а затем использовав их для расширения.
plist.insert(2, plist.pop(3)) #извлекаем пробел из списка и вставляем его обратно в список, но перед элементом с индексом 2,
new_phrase = ' '.join(plist)
print(plist)
print(new_phrase)