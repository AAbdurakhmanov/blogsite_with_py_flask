from datetime import datetime
from flask import (Flask, redirect, render_template, request, Response, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from werkzeug.exceptions import abort
from flask_migrate import Migrate, migrate
from flask_share import Share
from flask_user import UserManager, roles_accepted, roles_required, user_registered, login_required
import os


app = Flask(__name__)
app.config['SECRET_KEY'] = '4079d33f50e3492uig172216ghjkfd1947c3cab26'
app.config['SECURITY_PASSWORD_SALT'] = 'hpqohang;jgbiu2ug5t23bl4vrqwy'

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
app.config['SECURITY_POST_LOGIN'] = '/profile'
app.config['SOCIAL_FACEBOOK'] = {
    'consumer_key': 'facebook app id',
    'consumer_secret': 'facebook app secret'
}



db = SQLAlchemy(app)
share = Share(app)
migrate = Migrate(app, db)


class Blogpost(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  subtitle = db.Column(db.String(50))
  date_posted = db.Column(db.DateTime, default=datetime.utcnow)
  content = db.Column(db.Text)
  
