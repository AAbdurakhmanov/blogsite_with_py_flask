import datetime
import functools
import os
import re
import urllib
from flask import (Flask, abort, flash, Markup, redirect, render_template, request, Response, session, url_for)
from flask_sqlalchemy import SQLAlchemy
from flask.templating import render_template
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///data.db'
db = SQLAlchemy(app)

class Blogpost(db.model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(50))
  subtitle = db.Column(db.String(50))
  author = db.Column(db.String(20))
  date_posted = db.Column(db.DateTime)
  content = db.Column(db.Text)



# Route part
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/blog')
def blog():
  return render_template('blog.html')

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/some')
def some():
  return render_template('some.html')


# # Models part
# class Entry(db.Model):
#     title = CharField()
#     slug = CharField(unique=True)
#     content = TextField()
#     published = BooleanField(index=True)
#     timestamp = DateTimeField(default=datetime.datetime.now, index=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = re.sub('[^\w]+', '-', self.title.lower())
#         ret = super(Entry, self).save(*args, **kwargs)

#         # Store search content.
#         self.update_search_index()
#         return ret

#     def update_search_index(self):
#         search_content = '\n'.join((self.title, self.content))
#         try:
#             fts_entry = FTSEntry.get(FTSEntry.docid == self.id)
#         except FTSEntry.DoesNotExist:
#             FTSEntry.create(docid=self.id, content=search_content)
#         else:
#             fts_entry.content = search_content
#             fts_entry.save()


# class FTSEntry(FTSModel):
#     content = SearchField()

#     class Meta:
#         database = database


# # Forms part






if __name__ == '__main__':
  app.run(debug=True, port=5001)