#coading:uft8
from . import admin
from flask import render_template,redirect,url_for,flash,session,request
from werkzeug.security import generate_password_hash,check_password_hash
# 引入表单
from app.admin.forms import LoginForm,TagForm,MovieForm
from app.models import Admin,Tag,Movie
from functools import wraps
from app import db,app
from werkzeug.utils  import secure_filename
import os
import uuid
import datetime


@admin.route("/")
def index():
	return render_template("admin/index.html")

def change_filename(filename):
	fileinfo = os.path.splitext(filename)
	filename = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+str(uuid.uuid4().hex)+fileinfo[-1]
	return filename
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

#添加标签
@admin.route("/addtag/",methods=["GET","POST"])
def addtag():
	form = TagForm()
	if form.validate_on_submit():
		data = form.data
		tag = Tag.query.filter_by(name=data["name"]).count()
		if tag == 1:
			flash("标签已存在！","err")
			return redirect(url_for("admin.addtag"))
		t = Tag(name=data["name"])
		db.session.add(t)
		db.session.commit()
		flash("添加标签成功！","ok")
		return redirect(url_for("admin.addtag"))
	return render_template("admin/addtag.html",form=form)

#标签列表
@admin.route("/taglist/<int:page>/",methods=['GET'])
def taglist(page):
	if page is None:
		page = 1
	page_data = Tag.query.order_by(Tag.addtime.desc()).paginate(page=page, per_page=10)#per_page分页条数
	return render_template("admin/taglist.html",page_data=page_data)

#删除标签
@admin.route("/remove/tag/<int:id>/",methods=['GET'])
def removetag(id=None):
	tag = Tag.query.filter_by(id=id).first_or_404()
	db.session.delete(tag)
	db.session.commit()
	flash("删除标签成功！","ok")
	return redirect(url_for("admin.taglist",page=1))

#修改标签
@admin.route("/updatetag/<int:id>/",methods=['GET','POST'])
def updatetag(id=None):
	form = TagForm()
	tag = Tag.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		tag_count = Tag.query.filter_by(name=data["name"]).count()
		if tag.name != data["name"] and tag_count == 1:
			flash("标签名已存在","err")
			return redirect(url_for("admin.updatetag",id=id))
		tag.name=data["name"]
		db.session.add(tag)
		db.session.commit()
		flash("修改标签成功！","ok")
		return redirect(url_for("admin.updatetag",id=id))
	return render_template("admin/updatetag.html",id=id,form=form,t=tag)
#添加电影
@admin.route("/addfilm/",methods=['GET','POST'])
def addfilm():
	form = MovieForm()
	if form.validate_on_submit():
		data = form.data
		file_url = secure_filename(form.url.data.filename)
		file_logo = secure_filename(form.logo.data.filename)
		if not os.path.exists(app.config["UP_DIR"]):
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"],"rw")
		url = change_filename(file_url)
		logo = change_filename(file_logo)
		form.url.data.save(app.config["UP_DIR"]+url)
		form.logo.data.save(app.config["UP_DIR"]+logo)
		film = Movie.query.filter_by(title=data['title']).count()
		if film == 1:
			flash('片名已存在','err')
			return redirect(url_for('admin.addfilm'))
		movie =Movie(
			title=data['title'],
			url=url,
			info=data['info'],
			logo=logo,
			star=data['star'],
			playnum=0,
			commentnum=0,
			tag_id=data['tag_id'],
			area=data['area'],
			length=data['length'],
			release_time=str(data['release_time'])
		)
		db.session.add(movie)
		db.session.commit()
		flash('添加电影成功！','ok')
		return redirect(url_for('admin.addfilm'))
	return render_template("admin/addfilm.html",form=form)

@admin.route("/addforeshow/")
def addforeshow():
	return render_template("admin/addforeshow.html")

@admin.route("/commentslist/")
def commentslist():
	return render_template("admin/commentslist.html")

@admin.route("/userlist/")
def userlist():
	db.create_all()
	a = Admin(name="ymx",pwd=generate_password_hash("123"))
	t = Tag(name="爱情")
	db.session.add(a)
	db.session.add(t)
	db.session.commit()
	return("jgjhgvhjvhvh")
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
