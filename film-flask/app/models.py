#coading:uft8
from datetime import datetime
datetime.utcnow()
from app import db
from werkzeug.security import generate_password_hash,check_password_hash
db.drop_all()
db.create_all()
#会员
class User(db.Model):
	__tablename__ = "user"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	pwd=db.Column(db.String(100))
	email=db.Column(db.String(100),unique=True)
	phone=db.Column(db.String(11),unique=True)
	info=db.Column(db.String(255))
	face=db.Column(db.String(255),unique=True)
	addtime=db.Column(db.DateTime,index=True,default=datetime.utcnow)
	uuid=db.Column(db.String(255),unique=True)
	userlogs = db.relationship("Userlog", backref="user")
	comments = db.relationship("Comment", backref="user")
	moviecols = db.relationship("Moviecol", backref="user")

	def __repr__(self):
		return "<User %r>" % self.name

#会员登录日志
class Userlog(db.Model):
	__tablename__ = "userlog"
	id=db.Column(db.Integer,primary_key=True)
	user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
	ip = db.Column(db.String(100))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Userlog %r>" % self.id
#管理员
class Admin(db.Model):
	__tablename__ = "admin"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	pwd=db.Column(db.String(100))
	is_super=db.Column(db.SmallInteger) #是否为超级管理员，0表示超级管理员
	role_id =db.Column(db.Integer,db.ForeignKey('role.id'))#所属角色
	addtime=db.Column(db.DateTime,index=True,default=datetime.utcnow)
	adminlogs = db.relationship("Adminlog", backref="admin")
	oplogs = db.relationship("Oplog", backref="admin")

	def __repr__(self):
		return "<Admin %r>" % self.name


    #这种加密方法有问题  好像是基于对象的
	# #明文密码（只读）
	# @property
	# def password(self):
	# 	raise AttributeError(u'文明密码不可读')
	# #写入密码，同时计算hash值，保存到模型中
	# @password.setter
	# def password(self,value):
	# 	self._password=generate_password_hash("123")


    #检查密码函数
	def check_pwd(self,value):
		return check_password_hash(self.pwd,value)


#管理员登录日志
class Adminlog(db.Model):
	__tablename__ = "adminlog"
	id=db.Column(db.Integer,primary_key=True)
	admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))
	ip = db.Column(db.String(100))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Adminlog %r>" % self.id


#管理员操作日志
class Oplog(db.Model):
	__tablename__ = "oplog"
	id=db.Column(db.Integer,primary_key=True)
	admin_id = db.Column(db.Integer,db.ForeignKey("admin.id"))
	ip = db.Column(db.String(100))
	op = db.Column(db.String(100))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Oplog %r>" % self.id


#标签
class Tag(db.Model):
	__tablename__ = "tag"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)
	movies = db.relationship("Movie", backref="tag")

	def __repr__(self):
		return "<Tag %r>" % self.name


#电影
class Movie(db.Model):
	__tablename__ = "movie"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(255),unique=True)
	url=db.Column(db.String(255))
	info=db.Column(db.Text)
	logo=db.Column(db.String(255))
	playnum=db.Column(db.BigInteger)
	commentnum=db.Column(db.Integer)
	star=db.Column(db.SmallInteger)
	tag_id=db.Column(db.Integer, db.ForeignKey("tag.id"))
	area=db.Column(db.String(255))
	length=db.Column(db.String(255))
	release_time=db.Column(db.String(255))
	addtime = db.Column(db.DateTime,index=True, default="2018/05/06")
	comments = db.relationship("Comment", backref="movie")
	moviecols = db.relationship("Moviecol", backref="movie")

	def __repr__(self):
		return "<Movie %r>" % self.title


#预告
class Preview(db.Model):
	__tablename__ = "preview"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(255),unique=True)
<<<<<<< HEAD
	logo=db.Column(db.String(255),unique=True)
=======
>>>>>>> cf09bf1d82b1f969047e30178d8cc585efcc1b77
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Preview %r>" % self.title


#评论
class Comment(db.Model):
	__tablename__ = "comment"
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.Text)
	movie_id=db.Column(db.Integer, db.ForeignKey("movie.id"))
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Comment %r>" % self.id


#电影收藏
class Moviecol(db.Model):
	__tablename__ = "moviecol"
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.Text)
	user_id=db.Column(db.Integer, db.ForeignKey("user.id"))
	tag_id=db.Column(db.Integer, db.ForeignKey("movie.id"))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Moviecol %r>" % self.id


#权限
class Auth(db.Model):
	__tablename__ = "auth"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	url=db.Column(db.String(255),unique=True)
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)

	def __repr__(self):
		return "<Auth %r>" % self.name



#角色
class Role(db.Model):
	__tablename__ = "role"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	auths=db.Column(db.String(255))
	addtime = db.Column(db.DateTime,index=True, default=datetime.utcnow)


	def __repr__(self):
		return "<Role %r>" % self.name
