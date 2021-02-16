from quart import request, jsonify, Blueprint
from utils.meta import login, reset

auth_blueprint = Blueprint("auth", __name__)

@auth_blueprint.before_request
async def before_request():
    data = await request.get_json()
    if not data["license"]:
        return "", 400

# POST /auth/login
@auth_blueprint.route("/login", methods = ["POST"])
async def login_route():
    data = await request.get_json()

    key = data["license"]
    machine = data["machine"]

    if not key or not machine:
        return "", 400

    try:
        authResponse = login(key, machine)
        print(authResponse)
        return jsonify(authResponse)
    except Exception as e:
        print(e)
        return "", 400

# POST /auth/reset
@auth_blueprint.route("/reset", methods = ["POST"])
async def reset_route():
    data = await request.json

    key = data["license"]

    if not key:
        return "", 400

    try:
        authResponse = reset(key)
        return "", 200
    except Exception as e:
        print(e)
        return "", 400