
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

@app.route('/health')
def health():
    return 'This will be the health page.'


# if __name__ == "__main__":
#     app.run(debug=True)