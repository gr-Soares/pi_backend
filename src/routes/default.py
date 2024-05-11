from flask import Blueprint, jsonify

blueprint = Blueprint("default", __name__)


@blueprint.route("/", methods=["GET"])
def home():

    return (jsonify({"Data": {"status": 200, "title": "Hello Word"}}), 200)
