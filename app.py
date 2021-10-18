from models import *

# Route part
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/blog')
def blog():
  posts = Blogpost.query.order_by(Blogpost.title).all()
  return render_template('blog.html', posts=posts)

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/some')
def some():
  return render_template('some.html')


@app.route('/post/<int:post_id>')
def post(post_id):
  post = Blogpost.query.filter_by(id=post_id).one()
  return render_template('blog.html', post=post)

if __name__ == '__main__':
  app.run(debug=True, port=5001)