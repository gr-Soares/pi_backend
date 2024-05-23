from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter_no_token, flask_adapter
from src.controller import (
    create_avaliacao,
    list_avaliacao,
    update_avaliacao,
    delete_avaliacao,
    calculate_avaliacao
)

blueprint = Blueprint("avaliacao", __name__)


@blueprint.route("/avaliacao", methods=["POST"])
def create():
    response = flask_adapter(request=request, route=create_avaliacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/avaliacao", methods=["PUT"])
def update():
    response = flask_adapter(request=request, route=update_avaliacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/avaliacao", methods=["GET"])
def list():
    response = flask_adapter_no_token(request=request, route=list_avaliacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/avaliacao", methods=["DELETE"])
def delete():
    response = flask_adapter(request=request, route=delete_avaliacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )

@blueprint.route("/avaliacao/profissional", methods=["GET"])
def calculate():
    response = flask_adapter(request=request, route=calculate_avaliacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )