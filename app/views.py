from flask import render_template, flash, redirect, url_for
from app import app
from .forms import Fatu

@app.route('/')
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
@app.route('/ftu', methods=['GET', 'POST'])
def index():
    form = Fatu()
    user = {'nickname': 'Miguel'}
    if form.validate_on_submit():
        flash('Serching Twitter for the movie - "%s"' %
              (form.movie.data))
        mov = str(form.movie.data)
        return redirect(url_for('new'))
    return render_template("index.html",
                           title='Movie Sentiment Analysis',
                           user=user,
                           form=form)
@app.route('/iindex', methods=['GET', 'POST'])
def new():
    form = Fatu()
    user = {'nickname': 'FFatu'}
    if form.validate_on_submit():
        flash('Serching Twitter for the movie - "%s"' %
              (form.movie.data))
        mov = str(form.movie.data)
        return redirect(url_for('new'))
    return render_template('report.html',
                           title='wwwwww',
                           user=user,
                           form=form)
    
