#!/usr/bin/python3
"""Index that for the app status."""
from api.v1.views import app_views
from flask import jsonify
from models import storage
from models.engine import db_storage


@app_views.route('/status')
def status():
    """Statu method for the app statu."""
    statu = {"status": "OK"}
    return jsonify(statu)


@app_views.route('/stats')
def numbofobj():
    """NUMOFOBJ retrieves the number of each objects by type."""
    stats = {}

    for cls_name in db_storage.classes:
        count = storage.count(cls_name)
        stats[cls_name] = count

    return jsonify(stats)
