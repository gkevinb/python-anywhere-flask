from flask import Flask
import sys
import socket


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, Flask: {0}! on {1}'.format(sys.version, socket.gethostname())

@app.route('/health')
def health():
    return 'This will be the health page.'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)