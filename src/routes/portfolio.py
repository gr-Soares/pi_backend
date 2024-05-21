from flask import Blueprint, jsonify, request

from src.adapter import flask_adapter
from src.controller import (
    create_portfolio,
    list_portfolio,
    update_portfolio,
    delete_portfolio,
)

blueprint = Blueprint("portfolio", __name__)


@blueprint.route("/portfolio", methods=["POST"])
def create():
    response = flask_adapter(request=request, route=create_portfolio)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/portfolio", methods=["PUT"])
def update():
    response = flask_adapter(request=request, route=update_portfolio)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/portfolio", methods=["GET"])
def list():
    response = flask_adapter(request=request, route=list_portfolio)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )


@blueprint.route("/portfolio", methods=["DELETE"])
def delete():
    response = flask_adapter(request=request, route=delete_portfolio)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )
