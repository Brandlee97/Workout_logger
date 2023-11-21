from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)

# SQLALchemy database

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


if __name__ == "__main__":
    app.run(debug=True)