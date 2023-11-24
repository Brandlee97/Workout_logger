from flask import Flask, render_template, request, redirect, url_for, flash
from database import db, Workout


app = Flask(__name__)

# SQLALchemy database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///workout_database.db'
db.init_app(app)

with app.app_context():
    db.create_all()
    
# Home/About Page   **Done/Completed
@app.route('/')
def homepage():
    return render_template("home.html")

@app.route('/login')
def login():
    return render_template("login.html")

@app.route('/workout_form')
def workout_form():
    return render_template("workout_form.html")

# Create a submit new workout
@app.route('/saved_workout', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        muscle_group = request.form['muscle_group']
        exercise = request.form['exercise']
        sets = int(request.form['sets'])
        reps = int(request.form['reps'])

        created_workout = Workout(muscle_group=muscle_group, exercise=exercise, sets=sets, reps=reps)
        db.session.add(created_workout)
        db.session.commit()
    return redirect(url_for('workout_logs'))
    

# Look at past workouts
@app.route('/logged_workouts', methods=['GET', 'POST'])
def workout_logs():
    workouts = Workout.query.all()  
    print(workouts)
    return render_template("logged_workouts.html", workouts=workouts)

@app.route('/About_Us')
def aboutUs():
    return render_template("aboutUs.html")\
    
    
# Deleting and editing logs
@app.route('/delete/<int:workout_id>', methods=['GET','POST'])
def delete_exercise(workout_id):
    workout = Workout.query.get(workout_id)
    db.session.delete(workout)
    db.session.commit()
    flash("Exercise deleted")
    return redirect(url_for('workout_logs'))

@app.route('/edit/<int:workout_id>', methods=['GET', 'POST'])
def edit_exercise(workout_id):
    workout = Workout.query.get(workout_id)
    if workout:
        if request.method == 'POST':
            workout.muscle_group = request.form['muscle_group']
            workout.exercise = request.form['exercise']
            workout.sets = int(request.form['sets'])
            workout.reps = int(request.form['reps'])
            
            db.session.commit()

            flash("Exercise Edit Successful")
            return redirect(url_for('workout_logs'))
        else:
            return render_template('edit_workout.html', workout=workout)
    else:
        flash('Workout not found!')
        return redirect(url_for('logged_workouts'))
    

if __name__ == "__main__":
    app.run(debug=True)