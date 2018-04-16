#coading:uft8
from . import admin
from flask import render_template,redirect,url_for
@admin.route("/")
def index():
	return render_template("admin/index.html")

@admin.route("/login/")
def login():
	return render_template("admin/login.html")

@admin.route("/addtag/")
def addtag():
	return render_template("admin/addtag.html")

@admin.route("/taglist/")
def taglist():
	return render_template("admin/taglist.html")

@admin.route("/addfilm/")
def addfilm():
	return render_template("admin/addfilm.html")

@admin.route("/addforeshow/")
def addforeshow():
	return render_template("admin/addforeshow.html")

@admin.route("/commentslist/")
def commentslist():
	return render_template("admin/commentslist.html")

@admin.route("/userlist/")
def userlist():
	return render_template("admin/userlist.html")

@admin.route("/addadmin/")
def addadmin():
	return render_template("admin/addadmin.html")

@admin.route("/adminlist/")
def adminlist():
	return render_template("admin/adminlist.html")

@admin.route("/resetpassword/")
def resetpassword():
	return render_template("admin/resetpassword.html")