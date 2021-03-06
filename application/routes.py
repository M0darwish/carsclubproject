from application import app, db
from application.models import Members, Cars
from application.forms import CreateForm, UpdateForm, CreateCarForm, UpdateCarForm
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
def create_car():
    createcarform = CreateCarForm()
    members = Members.query.all()
    for member in members:
        createcarform.car_owner.choices.append((member.id, f"{member.name}"))

    if createcarform.validate_on_submit():
        car = Cars (plate=createcarform.plate.data, make=createcarform.make.data, member_id=createcarform.car_owner.data)
        db.session.add(car)
        db.session.commit()
        return redirect(url_for('read'))
    return render_template('create_car.html', form=createcarform)

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    member = Members.query.all()
    car = Cars.query.all()
    return render_template('read.html', members=member, cars=car)

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
    member = Members.query.filter_by(name=name).first()
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/delete_car/<plate>', methods=['GET', 'POST'])
def delete_car(plate):
    car = Cars.query.filter_by(plate=plate).first()
    db.session.delete(car)
    db.session.commit()
    return redirect(url_for('read'))

@app.route('/update/<name>', methods=['GET', 'POST'])
def update(name):
    updateform = UpdateForm()
    member = Members.query.filter_by(name=name).first()
    
    # Prepopulate the form boxes with current values when they open the page.
    if request.method == 'GET':
        updateform.name.data = member.name
        updateform.email.data = member.email
        return render_template('update.html', form=updateform)
    
    # Update the item in the databse when they submit
    else:
        if updateform.validate_on_submit():
            member.name = updateform.name.data
            member.email = updateform.email.data
            member.active = updateform.active.data
            db.session.commit()
            return redirect(url_for('read'))

@app.route('/update_car/<plate>', methods=['GET', 'POST'])
def update_car(plate):
    updatecarform = UpdateCarForm()
    car = Cars.query.filter_by(plate=plate).first()
    members = Members.query.all()
    for member in members:
        updatecarform.car_owner.choices.append((member.id, f"{member.name}"))

    # Prepopulate the form boxes with current values when they open the page (except members drop down list)
    if request.method == 'GET':
        updatecarform.plate.data = car.plate
        updatecarform.make.data = car.make
        updatecarform.car_owner.data= car.member_id
        return render_template('update_car.html', form=updatecarform)
    
    # Update the item in the databse when they submit
    else:
        if updatecarform.validate_on_submit():
            car.plate = updatecarform.plate.data
            car.make = updatecarform.make.data
            car.member_id=updatecarform.car_owner.data
            db.session.commit()
            return redirect(url_for('read'))

