#!/usr/bin/python3
"""script that starts a Flask web application"""


# import Flask class
from flask import Flask

# create an instance
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def index():
    """display "Hello HBNB!"

    Returns:
        str: text on the index page
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(debug=True)
