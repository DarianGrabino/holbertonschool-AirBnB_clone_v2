#!/usr/bin/python3
"""script that starts a Flask web application"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hbnb_c(text):
    c_text = text.replace("_", " ")
    return f"C {c_text}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def hbnb_python(text="is cool"):
    p_text = text.replace("_", " ")
    return f"Python {p_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def isint(n):
    return f"{n} is a number"


@app.route("/number_template/<int:n>")
def html_page(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
