from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class wourlout(db.model):
   id = db.Column(db.Integer, primary_key=True)

    muscle_group = db.Column(db.String(100), nullable=False)
    exercise = db.Column(db.string(100), nullable=False)
    sets = db.Column(db.Integer, nullable=False)
    reps = db.Column(db.Integer, nullable=False)

    