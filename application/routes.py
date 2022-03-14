
from application import app, db
from application.models import Members
from application.forms import CreateForm 

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

@app.route('/', methods=['GET'])
@app.route('/read', methods=['GET'])
def read():
    members = Members.query.all()
    return render_template('read.html', members=members)

@app.route('/delete/<name>', methods=['GET', 'POST'])
def delete(name):
    member = Members.query.filter_by(name=name).first()
    db.session.delete(member)
    db.session.commit()
    return redirect(url_for('read'))