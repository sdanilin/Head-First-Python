
from flask import Flask, render_template
from vsearch import search4letters

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask!'

@app.route('/search4')
def do_search() -> str:
    return str(search4letters('life, the univers, and everything', 'eiru,!'))

@app.route('/entry')
def entry_page() -> str:
    return render_template('entry_html',
                           the_title='Welcome tp search4letters on the web')

app.run()