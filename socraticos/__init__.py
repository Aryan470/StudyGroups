from firebase_admin import credentials, firestore
import firebase_admin
import json, os


cred = credentials.Certificate(json.loads(os.environ["PROJECT_AUTH"]))
firebase_admin.initialize_app(cred)
fireClient = firestore.client()

from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO(logger=True)

from socraticos.blueprints import users, groups, chat


def create_app():
    app = Flask(__name__)
    app.register_blueprint(users.users, url_prefix="/users")
    app.register_blueprint(groups.groups, url_prefix="/groups")
    socketio.init_app(app)
    return app
