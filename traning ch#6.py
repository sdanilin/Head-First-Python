tasks = open('todos.txt') #открыть файл, присвоить файловый поток переменной
for chore in tasks: #Выпонить некоторую обработку
    print(chore, end='')
tasks.close() #закрыть файл

with open('todos.txt') as task: #Инструкция with автоматически вызывает close
    for chore in task:
        print(chore, end='')