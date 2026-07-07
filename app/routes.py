from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from .db import (get_connection, 
                 get_all_interns, 
                 add_intern, 
                 delete_intern,
                 get_intern,
                 update_intern)

routes = Blueprint("routes", __name__)

@routes.route("/")
def login_page():
    if session.get("logged_in"):
        return redirect(url_for("routes.dashboard"))

    return render_template("login.html")

@routes.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")

    conn = get_connection()
    user = conn.execute(
        "SELECT * FROM users WHERE username = ?",
        (username,)
    ).fetchone()
    conn.close()

    if user and check_password_hash(user["password_hash"], password):
        session["logged_in"] = True
        session["username"] = user["username"]
        return redirect(url_for("routes.dashboard"))

    return render_template("login.html", error="Invalid username or password.")

@routes.route("/dashboard")
def dashboard():
    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))
    
    interns = get_all_interns()

    return render_template("dashboard.html", 
                           username=session["username"],
                           interns=interns)

@routes.route("/intern/add", methods=["POST"])
def create_intern():

    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))

    add_intern(request.form)

    return redirect(url_for("routes.dashboard"))

@routes.route("/intern/delete/<int:intern_id>", methods=["POST"])
def remove_intern(intern_id):

    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))

    delete_intern(intern_id)

    return redirect(url_for("routes.dashboard"))

@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.login_page"))

@routes.route("/edit/<int:intern_id>")
def edit_page(intern_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))

    intern = get_intern(intern_id)

    return render_template(
        "edit_intern.html",
        intern=intern
    )

@routes.route("/update/<int:intern_id>", methods=["POST"])
def update(intern_id):
    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))

    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "phone": request.form["phone"],
        "school": request.form["school"],
        "department": request.form["department"],
        "internship_start": request.form["internship_start"],
        "internship_end": request.form["internship_end"],
        "status": request.form["status"]
    }

    update_intern(intern_id, data)

    return redirect(url_for("routes.dashboard"))


