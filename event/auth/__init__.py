import jwt
from .models import User, Session
from functools import wraps
from flask import request, jsonify, current_app as app
from ..utils.security import escape
from .exceptions import TokenRequiredError, TokenMisMatchError, InvalidTokenError, TokenExpiredError

def decode_token():
	token = request.args.get('token', None)

	if not token:
		raise TokenRequiredError('Authentication token required.')

	token = escape(token)

	try:
		session = Session.query.filter_by(token=token).first()

		if not session:
			raise InvalidTokenError('Invalid Session.')

		# If user was logged out with this token
			# then don't let them log in
		if session.is_terminated():
			raise TokenExpiredError('Session has been expired, please login again.')

		payload = jwt.decode(token, app.config['SECRET_KEY'])
		user = payload['sub']

		user = User.query.get(user)

		if not user:
			raise TokenMisMatchError('Could not login with that token.')

		return user
	except jwt.ExpiredSignatureError:
		raise TokenExpiredError('Token has been expired. Please log in again.')
	except jwt.InvalidTokenError:
		raise InvalidTokenError('Invalid token.')

def authenticated_user():
	return decode_token()

def login_required(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		try:
			decode_token()
		except Exception as e:
			return jsonify(message=str(e), success=False), 440
		return f(*args, **kwargs)
	return decorated

def role_required(role):
	def wrapper(f):
		@wraps(f)
		def decorated(*args, **kwargs):
			# TODO (yashpokar) :: duplication is happening
				# replace with better solution
			try:
				user = authenticated_user()
			except Exception as e:
				return jsonify(message=str(e), success=False), 440

			if not user.has_role(role):
				return jsonify(message='You don\'t have rights to access this page.', success=False), 401
			return f(*args, **kwargs)
		return decorated
	return wrapper
