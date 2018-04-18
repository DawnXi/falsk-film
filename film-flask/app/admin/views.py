#coading:uft8
from . import admin
from flask import render_template,redirect,url_for,flash,session,request
from werkzeug.security import generate_password_hash,check_password_hash
# 引入表单
from app.admin.forms import LoginForm
from app.models import Admin

@admin.route("/")
def index():
	return render_template("admin/index.html")
# 登录
@admin.route("/login/",methods=["GET","POST"])
def login():
	# 实例化一个表单
	form = LoginForm()
	# 提交表单时进行前端验证
	if form.validate_on_submit():
		#获取表单数据
		data = form.data
		#取出对应的用户
		admin = Admin.query.filter_by(name=data['account']).first()
		#验证密码是否正确
		if not admin.check_pwd(data['pwd']):
			flash('密码错误！')
			return redirect(url_for('admin.login'))
		#验证通过  保存会话（保存已登录用户名）
		session['admin'] = data['account']
		#跳转到相应界面
		return redirect(request.args.get('next') or url_for('admin.index'))
	return render_template("admin/login.html",form=form)


@admin.route("/loginout/")
def loginout():
	form2 = LoginForm()
	from app import db
	from app.models import Admin
	admin =Admin(name='t58',pwd = generate_password_hash("456"))
	db.session.add(admin)
	db.session.commit()
	flash('注册成功')
	session.pop("account",None)#登出时删除会话
	return render_template("admin/login.html",form=form2)


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
