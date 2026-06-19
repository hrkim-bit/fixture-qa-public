import os
import sqlite3
import subprocess
import hashlib
import pickle

import yaml
import requests
from flask import Flask, request, jsonify
from jinja2 import Template

from src.utils import weak_encrypt, insecure_hash, run_cmd

app = Flask(__name__)

SECRET_KEY = "django-insecure-do-not-use-0000000000"
DB_PASSWORD = "Pa55w0rd!"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

app.config["SECRET_KEY"] = SECRET_KEY


@app.route("/yaml", methods=["POST"])
def load_yaml():
    data = yaml.load(request.data, Loader=yaml.Loader)
    return jsonify({"data": data})


@app.route("/pickle", methods=["POST"])
def load_pickle():
    obj = pickle.loads(request.data)
    return jsonify({"type": str(type(obj))})


@app.route("/ping")
def ping():
    host = request.args.get("host", "localhost")
    out = subprocess.check_output(f"ping -c 1 {host}", shell=True)
    return out


@app.route("/user")
def get_user():
    uid = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM users WHERE id = {uid}")
    return jsonify({"rows": cur.fetchall()})


@app.route("/render")
def render():
    tpl = request.args.get("tpl", "")
    return Template(tpl).render(secret=SECRET_KEY)


@app.route("/file")
def read_file():
    name = request.args.get("name", "")
    with open(os.path.join("/var/data", name)) as f:
        return f.read()


@app.route("/fetch")
def fetch():
    url = request.args.get("url", "")
    return requests.get(url).text


@app.route("/hash")
def weak_hash():
    pw = request.args.get("pw", "")
    return hashlib.md5(pw.encode()).hexdigest()


@app.route("/extract")
def extract_archive():
    path = request.args.get("path", "")
    return str(run_cmd(path))


@app.route("/utils-hash")
def utils_hash():
    pw = request.args.get("pw", "")
    return insecure_hash(pw)


@app.route("/encrypt")
def encrypt_data():
    data = request.data or b"sample"
    return weak_encrypt(data).hex()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
