from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, ValidationError

class CreateForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2,max=30)])
    email = StringField('Email', validators=[DataRequired(), Length(min=2,max=30)])
    submit = SubmitField('Register')