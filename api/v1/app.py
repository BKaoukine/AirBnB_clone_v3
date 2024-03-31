#!/usr/bin/python3
"""Falsk app."""

from api.v1.views import app_views
from flask import Flask
from flask import make_response
from flask import jsonify
from models import storage
import os


app = Flask(__name__)

app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_storage(exception):
    """Close the storage connection at the end of the request."""
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Handle the error response to retruns json instead of HTML."""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":

    host = os.environ.get('HBNB_API_HOST', '0.0.0.0')
    port = int(os.environ.get('HBNB_API_PORT', 5000))

    app.run(host=host, port=port, threaded=True)
