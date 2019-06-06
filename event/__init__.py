from celery import Celery
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate(db=db)
mail = Mail()
cors = CORS()

def create_app(config, include_blueprints=True):
	app = Flask(__name__)
	app.config.from_object(config)

	db.init_app(app)
	migrate.init_app(app)
	mail.init_app(app)
	cors.init_app(app,
		resources={'*': {
			'origins': app.config['ALLOWED_ORIGINS'],
			'Access-Control-Allow-Origin': app.config['ALLOWED_ORIGINS']
	}})

	if include_blueprints:
		from .errors.handlers import errors
		from .main.views import main
		from .auth.views import auth
		from .book.views import book

		app.register_blueprint(errors)
		app.register_blueprint(main)
		app.register_blueprint(auth)
		app.register_blueprint(book)

	return app

def make_celery(app=None):
	celery = Celery(
		app.import_name,
		backend=app.config['CELERY_RESULT_BACKEND'],
		broker=app.config['CELERY_BROKER_URL'],
	)
	celery.conf.update(app.config)

	class ContextTask(celery.Task):
		def __call__(self, *args, **kwargs):
			with app.app_context():
				return self.run(*args, **kwargs)

	celery.Task = ContextTask
	return celery
