from flask import Flask, render_template
import requests
from sqlalchemy import create_engine



app = Flask(__name__)

# SQLALchemy database
engine = create_engine("sqlite+pysqlite:///:memory:", echo=True)
with engine.connect() as conn:
    result = connexecute(text("selecct "))
# Home/About Page   **Done/Completed
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

# Create a new workout
@app.route('/create_workout')
def create():
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