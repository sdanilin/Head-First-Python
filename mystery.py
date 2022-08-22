"""В зависимости от ситуации, семантика вызовов функций в Python поддерживает оба способа передачи аргументов:
по значению и по ссылке."""
def double(arg):
    print('Befor: ', arg)
    arg = arg * 2 #Функция удваивает переданный аргумент
    print('After: ', arg)
# # num = 10
# # double(num)
# # Befor:  10
# # After:  20
# # num
# # 10
# # saying = 'Hello'
# # double(saying)
# # Befor:  Hello
# # After:  HelloHello
# # saying
# # 'Hello'
# # numbers = [42, 256, 16]
# # double(numbers)
# # Befor:  [42, 256, 16]
# # After:  [42, 256, 16, 42, 256, 16]
# # numbers
# # [42, 256, 16]


def change(arg):
    print('Befor: ', arg)
    arg.append('More date') #Функция добавляет строку в конец указанного списка
    print('After: ', arg)
    # numbers = [42, 256, 16]
    # change(numbers)
    # Befor: [42, 256, 16]
    # After: [42, 256, 16, 'More date']
    # numbers
    # [42, 256, 16, 'More date']