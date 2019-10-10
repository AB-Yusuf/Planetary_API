from flask import Flask, jsonify
from flask import request


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!, I am happy'


@app.route('/super')
def super_simple():
    return jsonify(message='Welcome to Planetary Api')


@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message='Sorry' + name + ', you are not old enough.'), 401
    else:
        return jsonify(message='Welcome ' + name + ', you are old enough.')
    

if __name__ == '__main__':
    app.run(debug=True)