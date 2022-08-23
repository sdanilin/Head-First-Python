import html
from flask import Flask, render_template, request #открывает доступ к переданным данным
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4', methods=['POST'])
def do_search() -> html:
    phrase = request.form['phrase'] #создаем новые переменные
    letters = request.form['letters'] #и присваиваем им данные из HTML формы
    title = 'Here are your results:'
    results = str(search4letters(phrase, letters))
    return render_template('results.html',
                            the_phrase=phrase,
                            the_letters=letters,
                            the_title=title,
                            the_results=results,)

@app.route('/entry')
def entry_page() -> html:
    return render_template('entry.html',
                           the_title='Welcome tp search4letters on the web!')

app.run(debug=True)
