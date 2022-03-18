from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(min=5,max=30)])
    submit = SubmitField('Register')

class UpdateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(min=5,max=30)])
    active = BooleanField('Active')
    submit = SubmitField('Update')
    
class CreateCarForm(FlaskForm):
    car_owner= SelectField ("Select a Member from the list* :", choices=[],validators=[DataRequired()])
    plate = StringField('Plate No', validators=[DataRequired(), Length(min=3,max=10)])
    make = StringField('Make', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Add')

class UpdateCarForm(FlaskForm):
    car_owner= SelectField ("Update the owner from members list* :", choices=[],validators=[DataRequired()])
    plate = StringField('Update Plate No', validators=[DataRequired(), Length(min=3,max=10)])
    make = StringField('Update Make', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Update')
