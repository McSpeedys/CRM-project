#This file will serve to host all the subpages for the website.
#Importing all necessary packages from flask
from flask import (
    Blueprint, 
    render_template,
    request,
    redirect,
    url_for,
    session,
)

#Importing werkzeug for password hashing.
from werkzeug.security import generate_password_hash, check_password_hash

#Blueprint setup for webpage routes.
routes = Blueprint("routes", name)

#Temporary admin creds.
ADMIN ={
    "username": "admin",
    "password_hash": ""generate_password_hash("password123")
}

#At the login page the server will render the login.html file.
@routes.route("/")
def login_page():
    if session.get("logged_in"):
        return redirect(url_for("routes.dashboard"))

    return render_template("login.html")

@routes.route("/login", methods=["POST"])
def login():
    username = request.form.get("username")
    password = request.form.get("password")
    
    #If username and password match send user to dashboard.
    if (username == ADMIN["username"] and check_password_hash(ADMIN["password_hash"], password)):
        session["logged_in"] = True
        session["username"] = username

        return redirect(url_for("routes.dashboard"))
    
    #Else send them back to the login page.
    return render_template("login.html", error="Invalid username or password.")
    

#At the dashboards page the server 
@routes.route("/dashboard")
def dashboard():
    #If user is not logged in or is trying to skip the login page without logging in send them back.
    if not session.get("logged_in"):
        return redirect(url_for("routes.login_page"))

    return render_template("dashboard.html", username=session["username"])

#Logout route
@routes.route("/logout")
def logout():
    session.clear()

    return redirect(url_for("routes.login_page"))
