from sqlalchemy import ForeignKey
from application import db

class Members(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False)
    active = db.Column(db.Boolean, default=False)
    cars = db.relationship('Cars', backref='member')

class Cars(db.Model):
    plate = db.Column(db.String(10), primary_key=True)
    make = db.Column(db.String(30), nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey('members.id'))
