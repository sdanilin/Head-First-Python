import html
from flask import Flask, render_template, request #открывает доступ к переданным данным
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phtase'] #создаем новые переменные
    letters = request.form['letters'] #и присваиваем им данные из HTML формы
    return str(search4letters(phrase, letters)) #используем эти переменные в вызове "search4letters"

@app.route('/entry')
def entry_page() -> html:
    return render_template('entry.html',
                           the_title='Welcome tp search4letters on the web')

app.run(debug=True)
