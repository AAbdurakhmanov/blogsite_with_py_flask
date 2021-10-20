from models import *
from flask_wtf import FlaskForm, Form
from wtforms import *
from wtforms import DateTimeField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_wtf.csrf import CSRFProtect, CSRFError


class AddpostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    subtitle = StringField('Subtitle', validators=[DataRequired()])
    date_posted = DateTimeField('Date posted', validators=[DataRequired()])
    content = TextField('Content', validators=[DataRequired()])
    submit = SubmitField('Send')
