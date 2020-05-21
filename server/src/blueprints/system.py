import sys
import socket
from flask import Blueprint, current_app, redirect


system = Blueprint('api', __name__)


@system.route('/')
def index():
    return redirect(current_app.config.get("WEB_HOST"), code=301)


@system.route('/system/info')
def hello_world():
    return 'Hello world, Flask: {0}! on {1}!'.format(sys.version, socket.gethostname())


@system.route('/system/health')
def health():
    return f"This is the health page. {current_app.config['HOST']}, {current_app.config['HOST_MACHINE']}"
