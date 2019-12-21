from flask import Flask, render_template, request
from authentication import Authentication
from drone_controller import DroneController
authentication = Authentication()
drone_controller = DroneController()


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


@app.route("/routing2", methods=["GET"])
def routing2():
    if request.values.get("add_drone"):
        return render_template("add_drone.html")
    elif request.values.get("view_drone"):
        display = drone_controller.display_drones()
        return "ok"
    elif request.values.get("move_drone"):
        return render_template("move_drone.html")
    elif request.values.get("get_distance"):
        return render_template("get_distance.html")
    else:
        return render_template("home.html")


@app.route("/new_user", methods=["GET"])
def new_user():
    username = request.values.get("username")
    password = request.values.get("password")
    true_or_false = authentication.new_user(username, password)
    if true_or_false == "Username already exists":
        username_already_exists = "username_already_exists"
        return render_template("exception_handling.html", username_already_exists=username_already_exists)
    return "ok"


@app.route("/login", methods=["GET"])
def login():
    username = request.values.get("username")
    password = request.values.get("password")
    true_or_false = authentication.authenticate(username, password)
    true_or_false = str(true_or_false)
    if true_or_false == "Username does not exist":
        username_does_not_exist = "username_does_not_exist"
        return render_template("exception_handling.html", username_does_not_exist=username_does_not_exist)
    elif true_or_false == "You are locked out of the system":
        locked_out = "locked_out"
        return render_template("exception_handling.html", locked_out=locked_out)
    elif true_or_false == "Welcome to the top secret system.":
        return render_template("controller.html")


@app.route("/add_drone", methods=["GET"])
def add_drone():
    drone_name = request.values.get("new_drone_name")
    test = drone_controller.add_drone(drone_name)
    test = str(test)
    if test == "Drone already exists":
        return "won't work"
    else:
        return "yes / create print function here"


@app.route("/move_drone", methods=["GET"])
def move_drone():
    drone_to_move = request.values.get("drone_to_move")
    if drone_to_move == "move_drone_not_found":
        move_drone_not_found = "move_drone_not_found"
        return render_template("exception_handling.html", move_drone_not_found=move_drone_not_found)
    try:
        move_x = int(request.values.get("x"))
        move_y = int(request.values.get("y"))
    except ValueError:
        value_error = "value_error"
        return render_template("exception_handling.html", value_error=value_error)
    drone_controller.move_drone(drone_to_move, move_x, move_y)
    return "create print function here"


if __name__ == '__main__':
    app.run()
