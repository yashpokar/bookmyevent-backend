from .. import db
from flask import Blueprint, jsonify, request, current_app as app
from .forms import (
	RegistrationForm,
	LoginForm,
	ForgotPasswordForm,
	ResetPasswordForm
)
from .models import User, Session
import jwt
from datetime import datetime, timedelta
from . import login_required
from .signals import user_registered, requested_for_password_reset
from ..utils.security import escape
from ..utils.request import extract, get_json

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
	form = RegistrationForm(get_json())

	if not form.validate():
		return jsonify(success=False, errors=form.errors, message='Validation fail.'), 422

	try:
		data = extract(form.data, 'first_name', 'last_name', 'email', 'phone', 'password')

		user = User(**data)
		user.set_password(data['password'])

		db.session.add(user)
		db.session.commit()

		user_registered.send(user)
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(success=True, message='Your account has been created successfully.', data=dict(user_id=user.id))

@auth.route('/email/<token>/verify', methods=['POST'])
def verify_email(token):
	user = User.verify_email_token(escape(token))

	if not user:
		return jsonify(success=False, message='Invalid email verification token.'), 422

	if user.email_verified_at:
		return jsonify(success=False, message='Your email has already been updated.'), 409

	try:
		user.email_verified_at = datetime.now()

		db.session.commit()
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(success=True, message='Your email has been verified successfully.')

@auth.route('/login', methods=['POST'])
def login():
	form = LoginForm(get_json())

	if not form.validate():
		return jsonify(errors=form.errors, success=False, message='Validation fail'), 422

	try:
		user = User.query.filter_by(email=escape(form.data['email'])).first()

		# Wrong user credentials
		if not user or not user.verify_password(escape(form.data['password'])):
			return jsonify(success=False, message='Please enter valid credentials.'), 401

		token = jwt.encode({
			'exp': datetime.now() + timedelta(hours=24),
			'iat': datetime.now(),
			'sub': user.id,
		}, app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')

		session = Session(user=user, token=token)

		db.session.add(session)
		db.session.commit()
	except:
		return jsonify(success=False, message='Internal server error'), 500

	return jsonify(success=True, token=token, message='You are logged in now.', user=dict(first_name=user.first_name, last_name=user.last_name))

@auth.route('/forgot_password', methods=['POST'])
def forgot_password():
	form = ForgotPasswordForm(get_json())

	if not form.validate():
		return jsonify(errors=form.errors, success=False, message='Validation fail'), 422

	try:
		user = User.query.filter_by(email=escape(form.data['email'])).first()

		requested_for_password_reset.send(user)
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(success=True, message='Email has been sent with instructions to reset your password.')

@auth.route('/reset_password/<token>', methods=['POST'])
def reset_password(token):
	form = ResetPasswordForm(get_json())

	if not form.validate():
		return jsonify(errors=form.errors, message='Validation fail', success=False), 422

	user = User.verify_reset_password_token(escape(token))

	if not user:
		return jsonify(message='Invalid reset password token.', success=False), 401

	try:
		user.set_password(escape(form.data['password']))

		db.session.commit()
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(success=True, message='Your password has been changed successfully.')

@auth.route('/logout', methods=['POST'])
@login_required
def logout():
	try:
		token = escape(request.args.get('token'))

		session = Session.query.filter_by(token=token).first()
		session.terminated_at = datetime.now()

		db.session.commit()
	except:
		return jsonify(success=False, message='Internal server error.'), 500

	return jsonify(success=True, message='Logged out successfully.')
