from flask import render_template, flash, redirect, url_for, request
from flask_pymongo import PyMongo
from urllib.request import urlopen
from app import app
import pygal
import json
from pygal.style import DarkSolarizedStyle
from bson import json_util
from .forms import Fatu

app.config['MONGO_DBNAME'] = 'flmdb'
app.config['MONGO_URI'] = 'mongodb://addmin:addmin@ds013414.mlab.com:13414/flmdb'

mongo = PyMongo(app)

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    form = Fatu()
    user = {'nickname': 'Miguel'}
    if form.validate_on_submit():
        flash('Serching Twitter for the movie - "%s"' %
              (form.movie.data))
        mov = str(form.movie.data)
        return redirect(url_for('get_weather_data', var=mov))
    return render_template("index.html",
                           title='Movie Sentiment Analysis',
                           user=user,
                           form=form)
@app.route('/report/<var>')
def get_weather_data(var):
        if len(var)>=3:
            return redirect(url_for('search', var=var))        
        return render_template('graph.html',
                           var=request.args.get('var'),
                           title=var)

@app.route('/search/<var>', methods=['GET', 'POST'])
def search(var):
        form = Fatu()
        ys = [6,7,9,4,5,8]
        xs = [2011,2012,2013,2014,2015,2016]
        user = mongo.db.users
        user.insert({'name' : var, 'year' : xs, 'rate' : ys})
        title = var
        bar_chart = pygal.Bar(width=800, height=400,
                          explicit_size=True, title=title,
                          style=DarkSolarizedStyle,
                          disable_xml_declaration=True)
        bar_chart.x_labels = xs
        bar_chart.add('Rating', ys)
        
        
        return render_template('report.html',
                           bar_chart=bar_chart,
                           var=request.args.get('var'),
                           form=form,
                           title=request.args.get('var'))
