from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter_no_token
from src.controller import (
    create_atuacao,
    list_atuacao,
    update_atuacao,
    delete_atuacao,
)

blueprint = Blueprint("atuacao", __name__)


@blueprint.route("/atuacao", methods=["POST"])
def create():
    response = flask_adapter_no_token(request=request, route=create_atuacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/atuacao", methods=["PUT"])
def update():
    response = flask_adapter_no_token(request=request, route=update_atuacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/atuacao", methods=["GET"])
def list():
    response = flask_adapter_no_token(request=request, route=list_atuacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/atuacao", methods=["DELETE"])
def delete():
    response = flask_adapter_no_token(request=request, route=delete_atuacao)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
