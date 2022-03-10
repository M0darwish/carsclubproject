from turtle import position
from application import app, db
from application.models import Members, Cars
from application.forms import CreateForm, CreateCarForm

from flask import render_template, redirect, url_for, request

@app.route('/create', methods=['GET', 'POST'])
def create():
    createform = CreateForm()

    if createform.validate_on_submit():
        member = Members (name=createform.name.data, email=createform.email.data)
        db.session.add(member)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create.html', form=createform)

@app.route('/create_car', methods=['GET', 'POST'])
def createcar():
    createcarform = CreateCarForm()
    members = Members.query.all()
    for member in members:
        createcarform.car_owner.choices.append((member.id, f"{member.name}"))

    if createcarform.validate_on_submit():
        car = Cars (plate=createcarform.plate.data, make=createcarform.make.data)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create_car.html', form=createcarform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    members = Members.query.all()
    return render_template('read.html', members=members)