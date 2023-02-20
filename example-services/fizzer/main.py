import time

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def fizz():
    time.sleep(.5)
    x = request.json["number"]
    fizz = bool(x % 3 == 0)
    return jsonify({"result": fizz})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
