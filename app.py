from flask import Flask, app, Blueprint, jsonify, redirect, request, url_for
from flask.templating import render_template
from werkzeug.exceptions import abort
import jinja2
app = Flask(__name__)

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


# Models part



# Forms part






if __name__ == '__main__':
  app.run(debug=True, port=5001)