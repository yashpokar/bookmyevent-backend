from .models import User
from flask_wtf import FlaskForm
from wtforms import StringField
from ..utils.validators import alphaspace, alphabetic, phone, Exists, Unique
from wtforms.validators import DataRequired, Length, Email, EqualTo


class ResetPasswordForm(FlaskForm):
	password = StringField(validators=[DataRequired(message='Password is required.'), Length(min=6, message='Password must have at least 6 characters.'), EqualTo('confirm_password', message='Password does not match.')])
	confirm_password = StringField()


class RegistrationForm(ResetPasswordForm):
	first_name = StringField(validators=[DataRequired(message='First name is required.'), Length(min=2, max=20, message='First name must be between 2 to 20 characters long.'), alphabetic])
	last_name = StringField(validators=[DataRequired(message='Last name is required.'), Length(min=2, max=20, message='Last name must be between 2 to 20 characters long.'), alphabetic])
	email = StringField(validators=[DataRequired(message='Email address is required.'), Email(message='Invalid email address.'), Length(max=255, message='Email address must be less than 255 characters long.'), Unique(User, 'email')])
	phone = StringField(validators=[DataRequired(message='Phone number is required.'), phone, Length(min=10, max=10, message='Phone number must have 10 digits.'), Unique(User, 'phone')])
	password = StringField(validators=[DataRequired(message='Password is required.'), Length(min=6, message='Password must have 6 characters at least.'), EqualTo('confirm_password', message='Password does not match.')])
	confirm_password = StringField()


class LoginForm(FlaskForm):
	email = StringField(validators=[DataRequired(message='Email address is required.'), Email(message='Please provide valid email address.')])
	password = StringField(validators=[DataRequired(message='Password is required.')])


class ForgotPasswordForm(FlaskForm):
	email = StringField(validators=[DataRequired(message='Email address is required.'), Email(message='Invalid email address.'), Exists(User, 'email')])
