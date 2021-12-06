from DBcm import UseDatabase
from sqlite3.dbapi2 import Cursor
from flask import Flask, render_template, request, escape
from werkzeug.utils import HTMLBuilder
from vsearch import search_for_letters


"""Identify the currently active namespace using __name__"""
app = Flask(__name__)

# BASE_DIR = os.path.dirname('/home/hkumar/Code/DB/')
# DB_PATH = os.path.join(BASE_DIR,"vsearchlogdb.db")

app.config['dbconfig'] = {}

def log_request(req: 'flask_request', res: str) -> None:
    """log th html requests and responses into a log file."""
    # conn = sqlite3.connect(DB_PATH)
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """insert into log(phrase, letters, ip, browser_string, results)
        values(?,?,?,?,?)"""

        cursor.execute(_SQL,(req.form['phrase'],
                        req.form['letters'],
                        req.remote_addr,
                        req.user_agent.browser,
                        res))


"""Use the @ before a function to identify it as a decorator. This lets you change the funtion's behavior
without changing the funtion's code"""


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    """This function invokes the search_for_letters module and maps the html field to the search_for_letters
    method as arguments, and renders the result on another html page."""
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your Results:'
    results = str(search_for_letters(phrase, letters))
    log_request(request, results)
    return render_template('results.html',
                           the_phrase=phrase,
                           the_letters=letters,
                           the_title=title,
                           the_results=results)


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html',
                           the_title='Welcome to search4letters on the Web!')


@app.route('/viewlog')
def view_the_log() -> 'html':
    """Display the log request from sqlite as a HTML table."""
    with UseDatabase(app.config['dbconfig']) as cursor:
        _SQL = """ select phrase, letters, ip, browser_string, results from log"""
        cursor.execute(_SQL)
        contents = cursor.fetchall()

    titles = ('Phrase', 'Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',
                           the_title='View Log',
                           the_row_titles=titles,
                           the_data=contents,)
    
    # contents = []
    # with open('vsearch.log') as log:
    #     for line in log:
    #         contents.append([])
    #         for item in line.split('|'):
    #             contents[-1].append(escape(item))
    # titles = ('Form Data', 'Remote_addr', 'User_agent', 'Results')
    # return render_template('viewlog.html',
    #                        the_title='View Log',
    #                        the_row_titles=titles,
    #                        the_data=contents,)


"""When deploying to a server, wrap the app.run(debug=True) in a dunder name == dunder main if statement."""
if __name__ == '__main__':
    app.run(debug=True)
