from flask import Flask, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

# SQLALchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///logindb.db'
db = SQLAlchemy(app)


class User(db.Model):
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100))

# Create database
with app.app_context():
    db.create_all()


# Home/About Page   **Done/Completed
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

# Create a new workout
@app.route('/create_workout')
def create():
    return render_template("create.html")

# Look at past workouts
@app.route('/logs')
def logs():
    return render_template("logs.html")


if __name__ == "__main__":
    app.run(debug=True)