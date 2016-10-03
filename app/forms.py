from flask_wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired

class Fatu(Form):
    movie = StringField('movie', validators=[DataRequired()])
