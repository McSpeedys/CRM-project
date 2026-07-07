from flask import Blueprint, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash
from .db import get_connection, get_all_interns

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

@routes.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("routes.login_page")) 
