from functools import wraps
from flask import request, make_response
import string
import random

TOKEN = None

def generate_auth_token(size=32):
    global TOKEN
    all_chars = string.ascii_letters + string.digits
    picked = random.choices(all_chars, k=size)
    TOKEN = "".join(picked)
    return TOKEN

def require_token(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        rec_token = request.args.get('auth', None)
        if TOKEN is not None and rec_token != TOKEN:
            return make_response({
                "message": "no_auth",
                "error": "Invalid / Missing access token."
            }, 401)
        else:
            return func(*args, **kwargs)
    return wrapper

def setup_auth(blueprint):
    @blueprint.before_request
    @require_token
    def auth_route():
        pass