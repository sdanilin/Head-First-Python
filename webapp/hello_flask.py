from flask import Flask

app = Flask(__name__) #Создание экземпляра объекта Flask и присваивание его переменной

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

app.run()