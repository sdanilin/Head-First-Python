# '''tarning to copy list'''
# '''Looks like a copy but it's not'''
# first = [1, 2, 3, 4, 5]
# print(first)
# second = first
# print(second)
# second.append(6) #erroe
# print(second)
# print(first) #error
#
# """How to copy the data strukture"""
# third = second.copy()
# print(third)
# third.append(7) # GOOD - new object add to list "third", but not to "first" and "second"
# print(third)
# print(second)


# '''traning [square brackets]'''
#
# saying = "Don't panic!"
# letters = list(saying)
# print(letters)
# print(letters[0])
# print(letters[3])
# print(letters[6])
# print(letters[-1])
# print(letters[-3])
# print(letters[-6])
# first = letters[0] #first object on list
# last = letters[-1] #last oject on list
# print(first)
# print(last)

# '''letters[start:stop:step] if start is empty = default = 0; if stop is empty = default = max index in list; step default = 1'''
# print(letters[0:10:3]) #except index 10
# print(letters[3:]) #show all letters except firts three
# print(letters[:10]) #show all letters befour (except) index 10
# print(letters[::2]) #every second letter

# '''Начало и конец диапазона в списке'''
book = "The Hitchhiker's Guide to the Galaxt"
booklist = list(book)
# print(booklist)
# print(booklist[0:3])
# booklist1 = booklist[0:3]
# booklist1 = ''.join(booklist1)
# print(booklist1)
# booklist2 = booklist[-6:]
# booklist2 = ''.join(booklist2)
# print(booklist2)

# '''Шаг диапазона в списке'''
# backwards = booklist[::-1] #перевернутая входная строка
# backwards = ''.join(backwards)
# print(backwards)
#
# every_over = booklist[::2] #срез данных
# every_over = "".join(every_over)
# print(every_over)
#
# booklist3 = booklist[4:14]
# booklist3 = ''.join(booklist3) #cut the word "Hitchhiker"
# print(booklist3)
# backward = booklist[13:3:-1]
# backward = ''.join(backward) #вырезать в обратном нарправлении
# print(backward)
