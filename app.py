# app.py

from flask import Flask, render_template
app = Flask(__name__)
context = {
    'caption': 'ГЛАВНАЯ СТРАНИЦА',
    'site': 'МОЙ БЛОГ',
    'home': 'ГЛАВНАЯ',
    'blog': 'БЛОГ',
    'contacts': 'КОНТАКТЫ',
    'users': ["Nina", "Karina", "Anton", "Nikita"]
}

@app.route('/shablon')
def shablon():
    return render_template('shablon.html', **context)

@app.route('/')
def index():
    return render_template('index.html', **context)
@app.route('/blog')
def blog():
    return render_template('blog.html', **context)
@app.route('/contacts')
def contacts():
    return render_template('contacts.html', **context)
if __name__ == '__main__':
    app.run(debug=True)