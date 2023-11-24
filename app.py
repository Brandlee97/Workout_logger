from flask import Flask, render_template
import requests
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqllalchemy.ext.declarative import declarative_base
from swlalchemy.orm import sessionmaker


app = Flask(__name__)

# SQLALchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout_database.db'
db.init_app(app)

# Home/About Page   **Done/Completed
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

# Create a new workout
@app.route('/create_workout', methods=[''])
def create():
    if request
    return render_template("create.html")

# Look at past workouts
@app.route('/logs')
def logs():
    return render_template("logs.html")

@app.route('/About_Us')
def aboutUs():
    return render_template("aboutUs.html")
if __name__ == "__main__":
    app.run(debug=True)