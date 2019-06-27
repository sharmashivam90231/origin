from flask import render_template
from app import app
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Anurag'}
    posts = [
    {'author': {'username': 'Karsimran'},
    'body': 'Beautiful day in Patiala!'
    },
    {
    'author': {'username': 'Jasmeet'},
    'body': 'The Avengers movie was so cool!'
    }
    ]
    return render_template('index.html', title='Home',
    user=user, posts=posts)