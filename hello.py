from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/whoami')
def whoami():
    return 'I am Michael D. Hoyle, 26 year old programmer, and lover of dogs.'

if __name__ == '__main__':
    app.run(debug=True)
