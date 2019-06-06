from .. import db


class Theater(db.Model):
	__tablename__ = 'theaters'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(255))


class Slot(db.Model):
	__tablename__ = 'slots'

	id = db.Column(db.Integer, primary_key=True)
	timing = db.Column(db.DateTime)
	day = db.Column(db.String(20))
	seat = db.Column(db.String(10))


class Ticket(db.Model):
	__tablename__ = 'tickets'

	id = db.Column(db.Integer, primary_key=True)
	type = db.Column(db.String(255))
	slot_id = db.Column(db.Integer, db.ForeignKey('slots.id'))
	theater_id = db.Column(db.Integer, db.ForeignKey('theaters.id'))
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
