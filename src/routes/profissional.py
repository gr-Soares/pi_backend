from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter, flask_adapter_no_token
from src.controller import (
    create_profissional,
    list_profissional,
    update_profissional,
    delete_profissional,
)

blueprint = Blueprint("profissional", __name__)


@blueprint.route("/profissional", methods=["POST"])
def create():
    response = flask_adapter_no_token(request=request, route=create_profissional)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/profissional", methods=["PUT"])
def update():
    response = flask_adapter(request=request, route=update_profissional)

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


@blueprint.route("/profissional", methods=["DELETE"])
def delete():
    response = flask_adapter(request=request, route=delete_profissional)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
