#This file will serve to host all the subpages for the website.
from flask import Blueprint, render_template

routes = Blueprint("routes", __name__)

#At the login page the server will render the login.html file.
@routes.route("/")
def login():
    return render_template("login.html")

#At the dashboards page the server 
@routes.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")
