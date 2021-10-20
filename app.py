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

@app.route('/add', methods=['GET', 'POST'])
def add():
  form = AddpostForm()
  if form.validate_on_submit():
      print('buniciii')
      p = Blogpost(
                    title = form.title.data,
                    subtitle = form.subtitle.data,
                    date_posted = datetime.now(),
                    content = form.content.data,
                  )
      db.session.add(p)
      db.session.commit()
      print('qoshildi bazaga')
      return redirect(url_for('index'))
      print('icida1')
      # return redirect(url_for('add'))
  return render_template('add.html', form=form)
  

@app.route('/posts/<int:post_id>')
def post(post_id):
  post = Blogpost.query.order_by(Blogpost.date_posted.desc()).all()
  return render_template('posts.html', form=form)



if __name__ == '__main__':
  app.run(debug=True, port=5001)