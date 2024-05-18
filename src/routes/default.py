from flask import Blueprint, jsonify, request
from src.adapter import flask_adapter_no_token
from ..controller.login import login_control

blueprint = Blueprint("default", __name__)


@blueprint.route("/", methods=["GET"])
def home():

    return (jsonify({"Data": {"status": 200, "title": "Hello Word"}}), 200)


@blueprint.route("/login", methods=["POST"])
def login():
    response = flask_adapter_no_token(request=request, route=login_control)

    if response.status_code < 300:
        return jsonify(response.body), response.status_code

    return (
        jsonify(
            {"error": {"status": response.status_code, "title": response.body["error"]}}
        ),
        response.status_code,
    )