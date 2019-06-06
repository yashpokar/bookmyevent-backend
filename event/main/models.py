from .. import db
from datetime import datetime
from sqlalchemy.ext.declarative import declared_attr


class RecordTrackerMixin:
	created_at = db.Column(db.DateTime, default=datetime.now())
	updated_at = db.Column(db.DateTime, onupdate=datetime.now())
	deleted_at = db.Column(db.DateTime)

	@declared_attr
	def created_by(cls):
		return db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

	@declared_attr
	def updated_by(cls):
		return db.Column(db.Integer, db.ForeignKey('users.id'))

	@declared_attr
	def deleted_by(cls):
		return db.Column(db.Integer, db.ForeignKey('users.id'))


class Image(db.Model, RecordTrackerMixin):
	__tablename__ = 'images'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String, nullable=False)
	imageable_id = db.Column(db.Integer, nullable=False)
	imageable_type = db.Column(db.String)
