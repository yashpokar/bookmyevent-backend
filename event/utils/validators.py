import re
from wtforms.validators import ValidationError

def alphaspace(form, field):
	if not any(s.isalpha() or s.isspace() for s in form.data):
		raise ValidationError(f'{" ".join(field.name.capitalize().split("_"))} should only contain alphabets and space.')

def alphabetic(form, field):
	if not field.data.isalpha():
		raise ValidationError(f'{" ".join(field.name.capitalize().split("_"))} should only contain alphabets.')


class Exists(object):
	def __init__(self, model, field):
		self.model = model
		self.field = field

	def __call__(self, form, field):
		record = getattr(getattr(self.model, 'query'), 'filter_by')(**{self.field: field.data}).count()

		if not record:
			raise ValidationError(f'{" ".join(field.name.capitalize().split("_"))} does not exists.')


class Unique(object):
	def __init__(self, model, field):
		self.model = model
		self.field = field

	def __call__(self, form, field):
		record = getattr(getattr(self.model, 'query'), 'filter_by')(**{self.field: field.data}).count()

		if record:
			raise ValidationError(f'{" ".join(field.name.capitalize().split("_"))} already exists.')


def phone(form, field):
	if not field.data.isnumeric():
		raise ValidationError('Invalid phone number.')

def url(form, field):
	pattern = re.compile(
		r'^(?:http|ftp)s?://' # http:// or https://
		r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
		r'localhost|' #localhost...
		r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		r'(?::\d+)?' # optional port
		r'(?:/?|[/?]\S+)$', re.IGNORECASE)

	if re.match(pattern, field.data) is not None:
		raise ValidationError('Invalid url.')
