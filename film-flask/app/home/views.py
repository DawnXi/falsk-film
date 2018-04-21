#coading:uft8
from . import home
from flask import render_template,redirect,url_for
@home.route("/")
def index():
	return render_template("home/index.html")

@home.route("/login/")
def login():
	return render_template("home/login.html")

@home.route("/loginout/")
def loginout():
	return redirect(url_for("home.login"))

@home.route("/user/")
def user():
	return render_template("home/user.html")

@home.route("/regist/")
def regist():
	return render_template("home/regist.html")

@home.route("/search/")
def search():
	return render_template("home/search.html")

@home.route("/play/")
def play():
	return render_template("home/play.html")