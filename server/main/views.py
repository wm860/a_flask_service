from flask import render_template, Blueprint, jsonify, request, redirect, url_for

from server.tasks import add_record_to_poll
from server.models import Db_service


main_blueprint = Blueprint("main", __name__,)


@main_blueprint.route("/", methods=["GET"])
def index():
    return render_template("main/index.html")


@main_blueprint.route("/poll", methods=["GET", "POST"])
def poll():
    if request.method == "GET":
        return render_template("main/poll.html")

    if request.method == "POST":
        username = request.form["username"]
        age = request.form["age"]
        city = request.form["city"]
        country = request.form["country"]
        task = add_record_to_poll.apply_async(args=[username, age, city, country])
        print(str(task))
        return redirect(url_for("main.results"))


@main_blueprint.route("/results", methods=["GET"])
def results():
    return render_template("main/results2.html")


@main_blueprint.route("/results2", methods=["GET"])
def results2():
    data = Db_service().get_last_record_from_poll()
    return render_template("main/results.html", data = data)

@main_blueprint.route("/login", methods=["GET"])
def login():
    return render_template("main/login.html")


@main_blueprint.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("main/register.html")

    if request.method == "POST":
        return redirect(url_for("main.index"))
