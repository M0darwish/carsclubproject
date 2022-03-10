from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Register')

class CreateCarForm(FlaskForm):
    car_owner= SelectField ("Select a Member from the list* :", choices=[],validators=[DataRequired()])
    plate = StringField('Plate', validators=[DataRequired(), Length(min=3,max=10)])
    make = StringField('Make', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Add')