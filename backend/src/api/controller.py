from typing import cast

from flask import Blueprint, g, jsonify, request

from src.api.auth import auth_required, generate_access_token
from src.datebase import User, Visits
from src.utlis import abort, validator

from .schemas import *

account = Blueprint(name="account", import_name=__file__, url_prefix="/account")
visitor = Blueprint(name="visitor", import_name=__file__)


@account.route("/users", methods=["POST"])
def post_user():
    if error := validator(request.json, schema_01):
        return abort(message=error)
    if User.query.filter_by(username=request.json["username"]).first():  # type: ignore
        return abort("This username has been used.", 400, "username")
    current_user = User.create(request.json["username"], request.json["password"])  # type: ignore
    response_data = current_user.to_dict()
    if error := validator(response_data, schema_02):
        return abort(message=error)
    return jsonify(response_data), 200


@account.route("/token", methods=["POST"])
def post_token():
    if error := validator(request.json, schema_03):
        return abort(message=error)
    current_user = User.query.filter_by(username=request.json["username"]).first()  # type: ignore
    if not current_user:
        return abort("No user found", 404, "username")
    if not cast(User, current_user).validate_password(cast(str, request.json["password"])):  # type: ignore
        return abort("Invalid password.", 401, "password")
    access_token = generate_access_token(cast(User, current_user))
    token_type = "Bearer"
    response_data = dict(accessToken=access_token, tokenType=token_type)
    if error := validator(response_data, schema_04):  # type: ignore
        return abort(message=error)
    return jsonify(response_data), 200


@account.route("/verify", methods=["GET"])
@auth_required
def verify_user():
    current_user = cast(User, g.current_user)
    current_user.extend_validity_period()
    response_data = current_user.to_dict()
    if validator(response_data, schema_02):
        return abort("Unauthenticated", 401)
    return jsonify(response_data), 200


@account.route("/user/<username>", methods=["GET"])
def get_user(username: str):
    current_user = User.query.filter_by(username=username).first()  # type: ignore
    if not current_user:
        return abort("No user found.", 404)
    response_data = cast(User, current_user).to_dict()
    if error := validator(response_data, schema_02):
        return abort(message=error)
    return jsonify(response_data), 200


@visitor.before_request
def increase_visits():
    visits = Visits.query.first()  # type: ignore
    cast(Visits, visits).increase()


@visitor.route("/home-visits")
def get_home_visits():
    visits = Visits.query.first()  # type: ignore
    return jsonify(cast(Visits, visits).count), 200
