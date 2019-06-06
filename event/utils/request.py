from flask import request
from .security import escape
from werkzeug.datastructures import ImmutableMultiDict

def get_json():
	try:
		return ImmutableMultiDict(request.json)
	except:
		# Json decode fail.
		pass

def extract(source, *keys):
	return { key: escape(source[key]) for key in keys }
