from flask import Flask, redirect

app = Flask(__name__)


@app.route("/register-product", methods=["GET"])
@app.route("/register-product/", methods=["GET"])
def register_product():
    return redirect("https://edwardsandco.nz/register-product", code=301)


@app.route("/", defaults={"path": ""}, methods=["GET"])
@app.route("/<path:path>", methods=["GET"])
def catch_all(path):
    return redirect("https://edwardsandco.nz/support", code=301)
