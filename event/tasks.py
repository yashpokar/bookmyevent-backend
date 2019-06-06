import os
from .config import ProductionConfig
from flask_mail import Message
from . import create_app, make_celery, mail

app = create_app(ProductionConfig, False)

celery = make_celery(app)

@celery.task
def send_email(subject, message, recipients: list):
	msg = Message(subject, recipients)
	msg.body = message

	return mail.send(msg)
