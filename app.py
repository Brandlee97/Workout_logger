from flask import Flask, redirect, url_for, render_template
#This is an example
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/library')
def user(name):
    return f"hello {name}"


@app.route('/new')
def admin():
    return redirect(url_for('user', name='Admin!'))

@app.route('/login')
def login():
    pass

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)