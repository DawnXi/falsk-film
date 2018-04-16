#coading:uft8
import datatime
from app import db
#会员
class User(db.Model):
	__tablename__ = "user"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	pwd=db.Column(db.String(100))
	email=db.Column(db.String(100),unique=True)
	phone=db.Column(db.String(11),unique=True)
	info=db.Column(db.Text)
	face=db.Column(db.String(255),unique=True)
	addtime=db.Column(db.DataTime,index=True,default=datatime.utcnow)
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
	user_id = db.Column(db.Integer,db.Foreignkey("user.id"))
	ip = db.Column(db.String(100))
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)

	def __repr__(self):
		return "<Userlog %r>" % self.id


#标签
class Tag(db.Model):
	__tablename__ = "tag"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)
	movies = db.relationship("Movie", backref="tag")

	def __repr__(self):
		return "<Tag %r>" % self.name	


#电影
class Movie(db.Model):
	__tablename__ = "movie"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(255),unique=True)
	url=db.Column(db.String(255),unique=True)
	info=db.Column(db.Tetx)
	logo=db.Column(db.String(255),unique=True)
	playnum=db.Column(db.BigInteger)
	commentnum=db.Column(db.BigInteger)
	star=db.Column(db.SmallInteger)
	tag_id=db.Column(db.BigInteger, db.Foreignkey("tag.id"))
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)
	comments = db.relationship("Comment", backref="movie")
	moviecols = db.relationship("Moviecol", backref="movie")

	def __repr__(self):
		return "<Movie %r>" % self.title


#预告
class Preview(db.Model):
	__tablename__ = "preview"
	id=db.Column(db.Integer,primary_key=True)
	title=db.Column(db.String(255),unique=True)
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)

	def __repr__(self):
		return "<Preview %r>" % self.title


#评论
class Comment(db.Model):
	__tablename__ = "comment"
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.Tetx)
	movie_id=db.Column(db.BigInteger, db.Foreignkey("movie.id"))
	user_id=db.Column(db.BigInteger, db.Foreignkey("user.id"))
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)
	
	def __repr__(self):
		return "<Comment %r>" % self.id


#电影收藏
class Moviecol(db.Model):
	__tablename__ = "comment"
	id=db.Column(db.Integer,primary_key=True)
	content=db.Column(db.Tetx)
	user_id=db.Column(db.BigInteger, db.Foreignkey("user.id"))
	tag_id=db.Column(db.BigInteger, db.Foreignkey("movie.id"))
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)
	
	def __repr__(self):
		return "<Moviecol %r>" % self.id


#权限
class Auth(db.Model):
	__tablename__ = "auth"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	url=db.Column(db.String(255),unique=True)
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)

	def __repr__(self):
		return "<Auth %r>" % self.name



#角色
class Role(db.Model):
	__tablename__ = "role"
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),unique=True)
	auths=db.Column(db.String(255))
	addtime = db.Column(db.DataTime,index=true, default=datatime.utcnow)

	def __repr__(self):
		return "<Role %r>" % self.name