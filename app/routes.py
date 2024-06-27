from app import app, db
from app.models import Post
from flask import render_template, request, flash, redirect, url_for
from app.forms import LoginForm

@app.route("/")
@app.route("/index")
def home():
    user = {"username": "David"}
    print(f"{url_for('home')} called")
    posts = [
        {
            'author': 'John',
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': 'Susan',
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title="Informus", user=user, posts=posts)

@app.route("/pgposts")
def posts_from_postgres():
    posts = Post.query.all()
    user = {"username": "David"}
    return render_template('index.html', title="Informus", user=user, posts=posts)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect('/index')
    return render_template('login.html', title='Login', form=form )