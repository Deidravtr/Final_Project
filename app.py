from flask import Flask, render_template, request

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


if __name__ == '__main__':
    app.run()
