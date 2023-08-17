#!/usr/bin/python3
"""This script starts a Flask web application"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays Hello"""
    return "Hello HBNB!"


if "__main__" == __name__:
    app.run(host='0.0.0.0', port=5000)
