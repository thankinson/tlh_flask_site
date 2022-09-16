from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email, ValidationError

class UserRegistration(FlaskForm):
    user_name = StringField('User Name: ', validators=[DataRequired(), Length(min=4, max=30)])
    first_name = StringField('First Name: ', validators=[DataRequired(), Length(min=2, max=30)])
    last_name = StringField('First Name: ', validators=[DataRequired(), Length(min=2, max=30)])
    user_email = StringField('Email: ', validators=[DataRequired(), Email(), Length(min=2)])
    password = PasswordField('Password: ', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password: ', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class UserLogin(FlaskForm):
    user_name = StringField('User Name: ', validators=[DataRequired(), Length(min=4, max=30)])
    password = PasswordField('Password: ', validators=[DataRequired()])
    remember_user = BooleanField('Remember Me :')
    submit = SubmitField('Login')