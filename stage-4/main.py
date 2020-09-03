"""
This module defines what will happen in stage-3.
"""
from flask import Flask, make_response, jsonify

app = Flask(__name__)


@app.route('/v2/predict', methods=['GET', 'POST'])
def predict():
    return make_response(jsonify({'y': 'hello_world'}))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
