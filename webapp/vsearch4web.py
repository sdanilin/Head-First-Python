import html
from flask import Flask, render_template, request #открывает доступ к переданным данным
from vsearch import search4letters

app = Flask(__name__)


def log_request(req: 'flask_request', res: str) -> None:
    '''Последние изменения, реализующие журналирование всех веб-запросов'''
    with open('vsaerch.log', 'a') as log:
        print(req, res, file=log)


@app.route('/search4', methods=['POST'])
def do_search() -> html:
    phrase = request.form['phrase'] #создаем новые переменные
    letters = request.form['letters'] #и присваиваем им данные из HTML формы
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    log_request(request, results) #Журнал хранится в файле "vsearclog"
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)

@app.route('/')
@app.route('/entry')
def entry_page() -> html:
    return render_template('entry.html',
                           the_title='Welcome tp search4letters on the web!')

@app.route('/viewlog') #Добавили новый URL
def view_the_log() -> str: #Объявили новую функцию, которая возващает строку
    with open('vsaerch.log') as log: #открыть файл для чтения логов
        contents = log.read()
    return contents


# if __name__ == '__main__':
app.run(debug=True) #вызов app.run производится только когда программа запускается непосредственно
