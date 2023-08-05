from flask import request, jsonify, Blueprint, make_response
from flask_cors import CORS
from .favorites import FavoritesManager

import os
from pathlib import Path

explorerBP = Blueprint('explorer', __name__)

HOMEDIR = str(Path.home())

def listdir(path, hidden=False):
    for f in os.listdir(path):
        if hidden:
            yield f
        elif not f.startswith('.'):
            yield f
    yield ".."

def getDirData(curPath, hidden=False):
    data = {
        'path': curPath,
        'entries': [],
    }

    for filename in listdir(curPath, hidden):
        filepath = os.path.join(curPath, filename)
        data['entries'].append({
            'name': filename,
            'path': filepath,
            'dir': os.path.isdir(filepath)
        })

    # Directories first, then files. Then sort by name, ignoring case.
    data['entries'].sort(key=lambda x: (1-x['dir'], x['name'].lower()))
    return jsonify(data)

@explorerBP.route("/path")
def route_get_subfolder():
    path = request.args.get('path', HOMEDIR)
    hidden = request.args.get('hidden', 'false') == 'true'
    curPath = os.path.abspath(path)
    return getDirData(curPath, hidden)

@explorerBP.route("/parent")
def route_get_parent():
    path = request.args.get('path', "/")
    hidden = request.args.get('hidden', 'false') == 'true'

    curPath = os.path.dirname(path)
    return getDirData(curPath, hidden)
    
FAVORITES = FavoritesManager()

@explorerBP.route("/favorites")
def route_get_favorites():
    return jsonify(FAVORITES.getFavorites())

@explorerBP.route("/favorites", methods=["POST"])
def route_add_favorite():
    path = request.args.get('path', None)
    if path is not None:
        FAVORITES.addFavorite(path)
    return jsonify(FAVORITES.getFavorites())

@explorerBP.route("/favorites", methods=["DELETE"])
def route_del_favorite():
    path = request.args.get('path', None)
    if path is not None:
        FAVORITES.removeFavorite(path)
    return jsonify(FAVORITES.getFavorites())

@explorerBP.errorhandler(Exception)
def route_exception_handler(exc):
    message = str(exc) + "\n- It's possible one of the favorites you selected has moved."
    return make_response({
        'message': message
    }, 400);