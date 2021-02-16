from quart import Quart, request, jsonify, redirect
from auth import auth_blueprint
from dotenv import load_dotenv

import os
import json
import signal
import secrets

#Makes it easy to exit with CTRL+C
signal.signal(signal.SIGINT, signal.SIG_DFL)

#Load Environment Variables
load_dotenv()

meta_api_key = os.getenv("META_API_KEY")

app = Quart(__name__)
app.secret_key = secrets.token_urlsafe(16)
app.register_blueprint(auth_blueprint, url_prefix = "/auth")

if not os.getenv("production") == "true":
    if meta_api_key is None:
        print("A Meta Labs API Key is required to start the server.")
        exit(0)
    else:
        app.run()