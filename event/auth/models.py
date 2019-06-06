from .. import db
from flask import current_app as app
from datetime import datetime
from passlib.hash import pbkdf2_sha256
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Session(db.Model):
	__tablename__ = 'sessions'

	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	token = db.Column(db.String(255), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now())
	terminated_at = db.Column(db.DateTime)

	user = db.relationship('User', back_populates='sessions')

	def is_terminated(self):
		return bool(self.terminated_at)


class User(db.Model):
	__tablename__ = 'users'

	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20), nullable=False)
	last_name = db.Column(db.String(20), nullable=False)
	email = db.Column(db.String(255), nullable=False, unique=True)
	phone = db.Column(db.String(20), nullable=False, unique=True)
	password = db.Column(db.String(255), nullable=False)
	email_verified_at = db.Column(db.DateTime)
	phone_verified_at = db.Column(db.DateTime)

	sessions = db.relationship('Session', back_populates='user')

	@property
	def name(self):
		return f'{self.first_name} {self.last_name}'

	def set_password(self, password):
		self.password = pbkdf2_sha256.hash(password)

	def verify_password(self, password):
		return pbkdf2_sha256.verify(password, self.password)

	def generate_password_reset_token(self, expires=1800):
		s = Serializer(app.config['SECRET_KEY'], expires_in=expires)
		return s.dumps({ 'user_id': self.id }).decode('utf-8')

	@staticmethod
	def verify_reset_password_token(token):
		s = Serializer(app.config['SECRET_KEY'])

		try:
			user_id = s.loads(token)['user_id']
		except:
			return
		return User.query.get(user_id)

	def generate_email_verification_token(self, expires=1800):
		return self.generate_password_reset_token(expires)

	@staticmethod
	def verify_email_token(token):
		return User.verify_reset_password_token(token)
