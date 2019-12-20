from flask import Flask, render_template, request
from authentication import Authentication
authentication = Authentication()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return render_template("home.html")


@app.route("/routing", methods=["GET"])
def routing():
    if request.values.get("login"):
        return render_template("login.html")
    elif request.values.get("new_user_account"):
        return render_template("new_user_account.html")


@app.route("/new_user", methods=["GET"])
def new_user():
    username = request.values.get("username")
    password = request.values.get("password")
    true_or_false = authentication.new_user(username, password)
    if true_or_false == "Username already exists":
        username_already_exists = "username_already_exists"
        return render_template("exception_handling.html", username_already_exists=username_already_exists)
    return "ok"


if __name__ == '__main__':
    app.run()
