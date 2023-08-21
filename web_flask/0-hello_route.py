#!/usr/bin/python3
""" This module defines a simple Flask Web Application"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=false)
def hello_hbtn():
    """ This function is executed whe the root URL ("/") is accessed """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)