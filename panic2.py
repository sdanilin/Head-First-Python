'''Методы списков изменяют состояние данных, а квадратные скобки и срезы нет'''

phrase = "Don't panic!"
plist = list(phrase)
print(phrase)
print(plist)
new_phrase = "".join(plist[1:3]) #cut 'on' from plist
new_phrase = new_phrase + ''.join([plist[5], plist[4], plist[7], plist[6]]) #cut every need object
print(plist)
print(new_phrase)