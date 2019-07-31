from flask import Flask, escape, request, render_template

app = Flask(__name__)

posts = [
    {
        'title': 'My First Post',
        'author': 'Sasha Kolomiytsev',
        'content': 'first post content',
        'date': '30th July 2019'
    },
    {
        'title': 'My Second Post',
        'author': 'Sasha Kolomiytsev',
        'content': 'second post content',
        'date': '31st July 2019'
    }
]

@app.route('/')
def hello():
    return '<h4>HELLO WORLD</h4>'

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/posts/<title>')
def posts(title):
    return render_template('post.html', posts=posts, title=title)
