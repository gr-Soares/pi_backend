from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter
from src.controller import create_cliente

blueprint = Blueprint("cliente", __name__)

@blueprint.route("/cliente", methods=["POST"])
def create():
    response = flask_adapter(request=request, route=create_cliente)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )