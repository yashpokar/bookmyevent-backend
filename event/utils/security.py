from flask import Markup

def escape(string):
	return str(Markup.escape(string)).strip()
