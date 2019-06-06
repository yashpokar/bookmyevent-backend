import os


class Config:
	WTF_CSRF_ENABLED = False
	SECRET_KEY = b'2H2B2|ES8kXKs{F[=U<4s>x%$PEAzV)Ec~]_j&)Ej(3<%6E3+l[a|,xQ<q=]mzP'
	SQLALCHEMY_TRACK_MODIFICATIONS = True

	REDIS_HOST = '127.0.0.1'
	REDIS_PORT = 6379
	REDIS_PASSWORD = None
	REDIS_DB = 0

	HOST = '0.0.0.0'
	PORT = 5000

	UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'storage/uploads/images/')

	ALLOWED_ORIGINS = '*'

	CELERY_BROKER_URL = 'redis://127.0.0.1:6379'
	CELERY_RESULT_BACKEND = 'redis://127.0.0.1:6379'

	MAIL_SERVER = 'smtp.mailtrap.io'
	MAIL_USERNAME = 'df78eae05c0a69'
	MAIL_PASSWORD = 'f8dc07e2882740'
	MAIL_PORT = 2525
	MAIL_USE_TLS = True
	MAIL_DEFAULT_SENDER = 'donotreply@kariyana.com'


class DevelopmentConfig(Config):
	ENV = 'development'
	DEBUG = True

	SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:password_here@127.0.0.1/bookmyevents'


class ProductionConfig(Config):
	ENV = 'production'
	DEBUG = False
	TESTING = False

	SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/test.db'
