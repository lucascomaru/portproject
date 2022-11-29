from flask import render_template, url_for
from portproject import app


@app.route('/')
def home ():
    return render_template('homepage.html')