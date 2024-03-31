#!/usr/bin/python3
"""States app."""

from flask import jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State
from flask import abort, request, jsonify


@app_views.route("/states", strict_slashes=False, methods=["GET"])
@app_views.route("/states/<state_id>", strict_slashes=False, methods=["GET"])
def states(state_id=None):
    """Show states and a specific state."""
    states_list = []
    if state_id is None:
        all_objs = storage.all(State).values()
        for v in all_objs:
            states_list.append(v.to_dict())
        return jsonify(states_list)
    else:
        result = storage.get(State, state_id)
        if result is None:
            abort(404)
        return jsonify(result.to_dict())


@app_views.route("/states/<state_id>", strict_slashes=False,
                 methods=["DELETE"])
def states_delete(state_id):
    """Delete method to delete a state."""
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    storage.delete(obj)
    storage.save()
    return jsonify({}), 200


@app_views.route("/states", strict_slashes=False, methods=["POST"])
def create_state():
    """Create a new post request for a state."""
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    if "name" not in data:
        abort(400, "Missing name")
    new_state = State(**data)
    new_state.save()
    return jsonify(new_state.to_dict()), 201


@app_views.route("/states/<state_id>", strict_slashes=False, methods=["PUT"])
def update_state(state_id):
    """Update state with id."""
    obj = storage.get(State, state_id)
    if obj is None:
        abort(404)
    data = request.get_json(force=True, silent=True)
    if not data:
        abort(400, "Not a JSON")
    obj.name = data.get("name", obj.name)
    obj.save()
    return jsonify(obj.to_dict()), 200
