from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter, flask_adapter_no_token
from src.controller import create_cliente, list_cliente, update_cliente, delete_cliente

blueprint = Blueprint("cliente", __name__)


@blueprint.route("/cliente", methods=["POST"])
def create():
    response = flask_adapter_no_token(request=request, route=create_cliente)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/cliente", methods=["PUT"])
def update():
    response = flask_adapter(request=request, route=update_cliente)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/cliente", methods=["GET"])
def list():
    response = flask_adapter(request=request, route=list_cliente)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/cliente", methods=["DELETE"])
def delete():
    response = flask_adapter(request=request, route=delete_cliente)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
