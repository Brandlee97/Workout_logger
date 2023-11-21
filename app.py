from flask import Flask, redirect, url_for, render_template
#This is an example
app = Flask(__name__)

# Home/About Page
@app.route('/')
def homepage():
    return render_template("home.html")

# Login Page
@app.route('/login') # Hello
@app.route('/library')
def user(name):
    return f"hello {name}"


@app.route('/new')
def new():
    return redirect("new.html")

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