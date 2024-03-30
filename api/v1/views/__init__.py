#!/usr/bin/python3
"""
API v1 package.

This package contains modules and resources related to API version 1.
"""

from flask import Blueprint

app_views = Blueprint("app_views", __name__, url_prefix="/api/v1")
from api.v1.views.index import *