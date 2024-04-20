from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter
from src.controller import create_profissional, list_profissional

blueprint = Blueprint("profissional", __name__)

@blueprint.route("/profissional", methods=["POST"])
def create():
    response = flask_adapter(request=request, route=create_profissional)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

@blueprint.route("/profissional", methods=["GET"])
def list():
    response = flask_adapter(request=request, route=list_profissional)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )