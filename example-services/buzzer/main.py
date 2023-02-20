from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["POST"])
def buzz():
    x = request.json["number"]
    buzz = bool(x % 5 == 0)
    return jsonify({"result": buzz})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6002)
