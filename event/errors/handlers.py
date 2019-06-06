from flask import Blueprint, jsonify
from werkzeug.exceptions import MethodNotAllowed

errors = Blueprint('errors', __name__)

@errors.app_errorhandler(MethodNotAllowed)
def handler_405(error):
	return jsonify(message='Method not allowed.', success=False), 405

@errors.app_errorhandler(404)
def handler_404(error):
	return jsonify(message='Page not found.', success=False), 404
