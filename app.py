from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLALchemy database

# Home/About Page
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/new')
def new():
    return render_template("new.html")

@app.route('/login')
def login():
    return render_template("login.html")

# Create a new workout
@app.route('/create')
def create():
    return render_template("create.html")

# Look at past workouts
@app.route('/history')
def history():
    return render_template("history.html")


if __name__ == "__main__":
    app.run(debug=True)