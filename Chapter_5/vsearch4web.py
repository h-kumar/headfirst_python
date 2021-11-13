from flask import Flask, render_template, request#, redirect
from werkzeug.utils import HTMLBuilder
from vsearch import search_for_letters

"""Identify the currently active namespace using __name__"""
app = Flask(__name__)

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

"""When deploying to a server, wrap the app.run(debug=True) in a dunder name == dunder main if statement."""
if __name__ == '__main__':
    app.run(debug=True)
