#!/usr/bin/python3
"""Index that for the app status."""
from api.v1.views import app_views
from flask import jsonify


@app_views.route('/status')
def status():
    """Statu method for the app statu."""
    statu = {"status": "OK"}
    return jsonify(statu)
