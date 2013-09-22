#!/usr/bin/env python
# encoding: utf-8

from flask import Blueprint


bp = Blueprint("home", __name__, url_prefix="/")


@bp.route("/")
def index():
    return "It works."
