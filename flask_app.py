from flask import Flask
import sys


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world, Flask: {}!'.format(sys.version)

@app.route('/health')
def health():
    return 'This will be the health page.'


# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug=True)