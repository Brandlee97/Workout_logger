from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# SQLALchemy database

# Home/About Page
@app.route('/')
def homepage():
    return render_template("home.html")

# Login Page
@app.route('/login')
def login():
    pass

# Create a new workout
@app.route('/create')
def create():
    pass

# Look at past workouts
@app.route('/history')
def history():
    pass

if __name__ == "__main__":
    app.run(debug=True)