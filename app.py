from datetime import date

from flask_wtf import form
from forms import *


@app.route('/')
def index():
  return render_template('index.html')

@app.route('/blog')
def blog():
  posts = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
  return render_template('blog.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/add')
def add():
  return render_template('add.html')  

@app.route('/addpost', methods=['POST'])
def addpost():
  form = AddpostForm()
  if form.validate_on_submit():
      
      post = Blogpost(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data, date_posted=datetime.utcnow())
      db.session.add(post)
      db.session.commit()
      return redirect(url_for('index'))
  return render_template('index.html', title='Home')


@app.route('/post/<int:post_id>')
def post(post_id):
  post = Blogpost.query.filter_by(id=post_id).one()
  return render_template('post.html', post=post)



if __name__ == '__main__':
  app.run(debug=True, port=5001)