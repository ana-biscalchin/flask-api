from flask import Flask, jsonify, request
import json


with open("./devs.json") as file_data:
    devs = json.load(file_data)


app = Flask(__name__)


@app.route("/devs", methods=["GET"])
def home():

    return jsonify(devs), 200


@app.route("/devs/<string:lang>", methods=["GET"])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev["lang"] == lang]

    return jsonify(devs_per_lang), 200


@app.route("/devs/<int:id>", methods=["GET"])
def devs_for_id(id):
    for dev in devs:
        if dev["id"] == id:
            return jsonify(dev), 200

    return jsonify({"error": "nao achou"}), 404


@app.route("/devs/<int:id>", methods=["PUT"])
def change_lang(id):
    for dev in devs:
        if dev["id"] == id:
            dev["lang"] = request.get_json().get("lang")
            return jsonify(dev), 200

    return jsonify({"error": "dev not found"}), 404


@app.route("/devs", methods=["POST"])
def save_dev():
    data = request.get_json()
    devs.append(data)

    return jsonify(data), 201


@app.route("/devs/<int:id>", methods=["DELETE"])
def remove_dev(id):
    index = id
    del devs[index]

    return jsonify({"message": "dev is no longer alive"}), 200


if __name__ == "__main__":
    app.run(debug=True)
