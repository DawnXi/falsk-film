#coading:uft8
from . import admin
from flask import render_template,redirect,url_for,flash,session,request
from werkzeug.security import generate_password_hash,check_password_hash
# 引入表单
<<<<<<< HEAD
from app.admin.forms import LoginForm,TagForm,MovieForm,PreviewForm,AdminForm,MoviecolForm,AuthForm,UserForm,RoleForm,PwdForm
from app.models import Admin,Tag,Movie,Preview,User,Comment,Role,Auth,Oplog,Adminlog,Userlog,Moviecol


from functools import wraps
from app import db,app
from werkzeug.utils import secure_filename
=======
from app.admin.forms import LoginForm,TagForm,MovieForm
from app.models import Admin,Tag,Movie
from functools import wraps
from app import db,app
from werkzeug.utils  import secure_filename
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
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
<<<<<<< HEAD
	#查询出数据并设置分页大小，将数据集传到视图
=======
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
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
<<<<<<< HEAD

=======
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
#添加电影
@admin.route("/addfilm/",methods=['GET','POST'])
def addfilm():
	form = MovieForm()
	if form.validate_on_submit():
		data = form.data
<<<<<<< HEAD
		film = Movie.query.filter_by(title=data['title']).count()
		if film == 1:
			flash('片名已存在','err')
			return redirect(url_for('admin.addfilm'))
		#文件路径的处理
		#secure_filename不支持中文（todo）
		# file_url = secure_filename(form.url.data.filename)
		# file_logo = secure_filename(form.logo.data.filename)
		file_url = form.url.data.filename
		file_logo = form.logo.data.filename
		url = change_filename(file_url)
		logo = change_filename(file_logo)
		if not os.path.exists(app.config["UP_DIR"]):
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"],"rw")
		form.url.data.save(app.config["UP_DIR"]+url)
		form.logo.data.save(app.config["UP_DIR"]+logo)
=======
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
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
		movie =Movie(
			title=data['title'],
			url=url,
			info=data['info'],
			logo=logo,
<<<<<<< HEAD
			star=int(data['star']),
			playnum=0,
			commentnum=0,
			tag_id=int(data['tag_id']),
=======
			star=data['star'],
			playnum=0,
			commentnum=0,
			tag_id=data['tag_id'],
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
			area=data['area'],
			length=data['length'],
			release_time=str(data['release_time'])
		)
		db.session.add(movie)
		db.session.commit()
		flash('添加电影成功！','ok')
		return redirect(url_for('admin.addfilm'))
	return render_template("admin/addfilm.html",form=form)

<<<<<<< HEAD
#电影列表
@admin.route("/movie/list/<int:page>",methods=['GET'])
def movielist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Movie.query.join(Tag).filter(
	#表连接查询标签
	Tag.id == Movie.tag_id
	).order_by(
	Movie.addtime.desc()
	).paginate(page=page, per_page=5)#per_page分页条数
	return render_template("admin/movielist.html",page_data=page_data)


#修改电影
@admin.route("/update/movie/<int:id>/",methods=['GET','POST'])
def updatemovie(id=None):
	form = MovieForm()
	movie = Movie.query.get_or_404(id)
	#对value属性无法修改的属性值进行修改
	if request.method == "GET":
		form.info.data = movie.info
		form.tag_id.data = movie.tag_id
		form.star.data = movie.star
		form.url.data = movie.url
		form.logo.data = movie.logo

	if form.validate_on_submit():
		data = form.data
		m_count = Movie.query.filter_by(title=data["title"]).count()
		if  m_count == 1:
			flash("同名电影已存在！","err")
			return redirect(url_for("admin.updatemovie",id=id))
		if not os.path.exists(app.config["UP_DIR"]):
			os.makedirs(app.config["UP_DIR"])
			os.chmod(app.config["UP_DIR"],"rw")

		if form.url.data.filename !="":
			file_url = form.url.data.filename
			url = change_filename(file_url)
			movie.url=url
			form.url.data.save(app.config["UP_DIR"]+url)

		if form.logo.data.filename !="":
			file_logo = form.logo.data.filename
			logo = change_filename(file_logo)
			movie.logo=logo
			form.logo.data.save(app.config["UP_DIR"]+logo)
		movie.title=data["title"]
		#movie.url=strftime(data["url"])
		movie.info=data["info"]
		#movie.logo=strftime(data["logo"])
		movie.star=int(data["star"])
		movie.tag_id=int(data["tag_id"])
		movie.area=data["area"]
		movie.length=data["length"]
		movie.release_time=data["release_time"]
		db.session.add(movie)
		db.session.commit()
		flash("修改电影成功！","ok")
		return redirect(url_for("admin.updatemovie",id=id))
	return render_template("admin/updatemovie.html",form=form,m=movie)

#删除电影
@admin.route("/remove/movie/<int:id>/",methods=['GET'])
def removemovie(id=None):
	movie = Movie.query.get_or_404(id)
	db.session.delete(movie)
	db.session.commit()
	#找到电影对应的静态资源并删除
	os.remove(app.config["UP_DIR"]+movie.url)
	os.remove(app.config["UP_DIR"]+movie.logo)
	flash("删除电影成功！","ok")
	return redirect(url_for("admin.movielist",page=1))


#添加预告（todo）
@admin.route("/addpr/",methods=["GET","POST"])
def addpr():
	form = PreviewForm()
	if form.validate_on_submit():
		data=form.data
		p_count = Preview.query.filter_by(title=data["title"]).count()
		if p_count == 1:
			flash("预告名已存在！","err")
			return redirect(url_for("admin.addpr"))
		preview = Preview(title=data["title"])
		db.session.add(preview)
		db.session.commit()
		flash("添加预告成功","ok")
		return redirect(url_for("admin.addpr"))
	return render_template("admin/addpr.html",form=form)

#预告列表
@admin.route("/previewlist/<int:page>/",methods=['GET'])
def previewlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Preview.query.order_by(Preview.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/previewlist.html",page_data=page_data)

#修改预告(todo)
@admin.route("/updatepreview/<int:id>/",methods=['GET','POST'])
def updatepreview(id=None):
	form = PreviewForm()
	preview = Preview.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		preview_count = Preview.query.filter_by(title=data["title"]).count()
		if  preview_count == 1:
			flash("预告名已存在","err")
			return redirect(url_for("admin.updatepreview",id=id))
		preview.title=data["title"]
		db.session.add(preview)
		db.session.commit()
		flash("修改预告成功！","ok")
		return redirect(url_for("admin.updatepreview",id=id))
	return render_template("admin/updatepreview.html",id=id,form=form,p=preview)

#删除预告
@admin.route("/removepreview/<int:id>/",methods=['GET'])
def removepreview(id=None):
	p = Preview.query.filter_by(id=id).first_or_404()
	db.session.delete(p)
	db.session.commit()
	flash("删除预告成功！","ok")
	return redirect(url_for("admin.previewlist",page=1))


#用户列表
@admin.route("/userlist/<int:page>/",methods=['GET'])
def userlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = User.query.order_by(User.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/userlist.html",page_data=page_data)


#修改用户
@admin.route("/updateuser/<int:id>",methods=["GET","POST"])
def updateuser(id=None):
	form = UserForm()
	user = User.query.get_or_404(id)
	if form.validate_on_submit():
		if form.validate_on_submit():
			data = form.data
			u_count = User.query.filter_by(name=data["name"]).count()
			if u_count == 1:
				flash("用户名已存在","err")
				return redirect(url_for("admin.updateuser",id=id))
			user.name=data["name"]
			user.pwd=generate_password_hash(data["pwd"])
			db.session.add(user)
			db.session.commit()
			flash("修改用户成功！","ok")
			return redirect(url_for("admin.updateuser",id=id))
	return render_template("admin/updateuser.html",form=form,u=user,id=id)


#删除用户
@admin.route("/removeuser/<int:id>",methods=["GET","POST"])
def removeuser(id=None):
	user = User.query.filter_by(id=id).first_or_404()
	db.session.delete(user)
	db.session.commit()
	flash("删除用户成功！","ok")
	return redirect(url_for("admin.userlist",page=1))


#评论列表
@admin.route("/commentlist/<int:page>/",methods=['GET'])
def commentlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Comment.query.order_by(Comment.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/commentlist.html",page_data=page_data)


#删除评论
@admin.route("/removecomment/<int:id>/",methods=['GET','POST'])
def removecomment(id):
	comment = Comment.query.get_or_404(id)
	db.session.delete(comment)
	db.session.commit()
	flash("删除评论成功！","ok")
	return redirect(url_for("admin.commentlist",page=1))

#收藏列表
@admin.route("/moviecollist/<int:page>/",methods=['GET'])
def moviecollist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Moviecol.query.order_by(Moviecol.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/moviecollist.html",page_data=page_data)

#编辑收藏
@admin.route("/updatemoviecol/<int:id>/",methods=['GET','POST'])
def updatemoviecol(id=None):
	form = MoviecolForm()
	moviecol = Moviecol.query.get_or_404(id)
	if form.validate_on_submit():
		data = form.data
		moviecol.content=data["content"]
		db.session.add(moviecol)
		db.session.commit()
		flash("修改收藏成功！","ok")
		return redirect(url_for("admin.updatemoviecol",id=id))
	return render_template("admin/updatemoviecol.html",id=id,form=form,m=moviecol)


#删除收藏
@admin.route("/removemoviecol/<int:id>/",methods=['GET','POST'])
def removemoviecol(id):
	moviecol = Moviecol.query.get_or_404(id)
	db.session.delete(moviecol)
	db.session.commit()
	flash("删除评论成功！","ok")
	return redirect(url_for("admin.moviecollist",page=1))


#添加管理员
@admin.route("/addadmin/",methods=["GET","POST"])
def addadmin():
	form = AdminForm()
	if form.validate_on_submit():
		data=form.data
		a_count = Admin.query.filter_by(name=data["name"]).count()
		if a_count == 1:
			flash("管理员已存在！","err")
			return redirect(url_for("admin.addadmin"))
		admin = Admin(
			name=data["name"],
			pwd=generate_password_hash(data["pwd"])
		)
		db.session.add(admin)
		db.session.commit()
		flash("添加管理员成功","ok")
		return redirect(url_for("admin.addadmin"))
	return render_template("admin/addadmin.html",form=form)

#管理员列表
@admin.route("/adminlist/<int:page>/",methods=['GET'])
def adminlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Admin.query.order_by(Admin.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/adminlist.html",page_data=page_data)


#用户登录日志列表
@admin.route("/userloginlist/<int:page>/",methods=['GET'])
def userloginlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Userlog.query.order_by(Userlog.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/userloginlist.html",page_data=page_data)

#管理员登陆日志列表
@admin.route("/adminloginlist/<int:page>/",methods=['GET'])
def adminloginlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Adminlog.query.order_by(Adminlog.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/adminloginlist.html",page_data=page_data)

#操作日志列表
@admin.route("/oplist/<int:page>/",methods=['GET'])
def oplist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Oplog.query.order_by(Oplog.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/oplist.html",page_data=page_data)


#添加权限
@admin.route("/addauth/",methods=["GET","POST"])
def addauth():
	form = AuthForm()
	if form.validate_on_submit():
		data = form.data
		a_count = Auth.query.filter_by(name=data["name"]).count()
		if a_count == 1:
			flash("标签已存在！","err")
			return redirect(url_for("admin.addauth"))
		auth = Auth(name=data["name"])
		db.session.add(auth)
		db.session.commit()
		flash("添加标签成功！","ok")
		return redirect(url_for("admin.addauth"))
	return render_template("admin/addauth.html",form=form)

#权限列表
@admin.route("/authlist/<int:page>/",methods=['GET'])
def authlist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Auth.query.order_by(Auth.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/authlist.html",page_data=page_data)

#添加角色
@admin.route("/addrole/",methods=['GET','POST'])
def addrole():
	form = RoleForm()
	if form.validate_on_submit():
		data = form.data
		a_count = Auth.query.filter_by(name=data["name"]).count()
		if a_count == 1:
			flash("角色已存在！","err")
			return redirect(url_for("admin.addrole"))
		role = Role(name=data["name"])
		db.session.add(role)
		db.session.commit()
		flash("添加角色成功！","ok")
		return redirect(url_for("admin.addrole"))
	return render_template("admin/addrole.html",form=form)

#角色列表
@admin.route("/rolelist/<int:page>/",methods=['GET'])
def rolelist(page):
	if page is None:
		page = 1
	#查询出数据并设置分页大小，将数据集传到视图
	page_data = Role.query.order_by(Role.addtime.desc()).paginate(page=page, per_page=1)#per_page分页条数
	return render_template("admin/rolelist.html",page_data=page_data)

#修改密码
@admin.route("/resetpassword/",methods=['GET','POST'])
def resetpassword():
	form=PwdForm()
	if form.validate_on_submit():
		data = form.data
		admin = Admin.query.filter_by(name=session['admin']).first()
		admin.pwd = generate_password_hash(data['new_pwd'])
		db.session.add(admin)
		db.session.commit()
		flash("修改密码成功！,请重新登录","ok")
		redirect(url_for('admin.loginout'))
	return render_template("admin/resetpassword.html",form=form)
=======
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
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
