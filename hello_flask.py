from flask import Flask
from vsearch import search4letters

app = Flask(__name__) #Создание экземпляра объекта Flask и присваивание его переменной

@app.route('/') # ('/') - это URL. Декоратор функции (начинается с @)- настраивает поведение существующей функции без изменения кода самой функции
def hello() -> str: #Функция возвращающая строку
    return 'Hello world from Flask!'

@app.route('/search4') # декоратор устанавливает URL
def do_search() -> str:
    return str(search4letters('life, the universe, and everything', 'eiru,!')) #Функция do_search вызывает search4letters и возвращает результат в виде строки

app.run() #Строка предлагает объекту Flask в переменной app запустить веб-сервер, вызывая метод run