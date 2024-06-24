from app import app
from flask import render_template

@app.route("/")
def home():
    user = {"username": "David"}
    return render_template('index.html', title="Informus", user=user)
