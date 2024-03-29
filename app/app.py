import sys

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    version = "{}.{}".format(sys.version_info.major, sys.version_info.minor)
    message = "Oli".format(
        version
    )
    return message


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)