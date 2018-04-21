#coading:uft8
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,FileField,TextAreaField,SelectField
from wtforms.validators import DataRequired,ValidationError
from app.models import Admin,Movie,Tag,Auth

tags = Tag.query.all()
auth = Auth.query.all()


class LoginForm(FlaskForm):
	# 管理员登录表单
	account = StringField(
		"账号",
		validators=[
			DataRequired("请输入账号！！！")
		],
		description="账号",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入账号！!!",
			#"required":"required"
		}
	)

	pwd = PasswordField(
		"密码",
		validators=[
			DataRequired("请输入密码！!!")
		],
		description="密码",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入密码！!!",
			#"required":"required"
		}
	)

	submit = SubmitField(
		"登录",
		render_kw={
			"class":"btn btn-primary btn-block",
		}
	)

	def validate_account(self,field):
		account = field.data
		admin = Admin.query.filter_by(name=account).count()
		if admin == 0:
			raise ValidationError("账号不存在！")

class TagForm(FlaskForm):
	name = StringField(
		label="标签名",
		validators=[
			DataRequired("请输入标签名!!!")
		],
		description='标签',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入标签名！"
		}
	)

	submit = SubmitField(
		label="添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)



class MovieForm(FlaskForm):
	title = StringField(
		label="片名",
		validators=[
			DataRequired("请输入片名!!!")
		],
		description='标签',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入片名！"
		}
	)

	url = FileField(
		label="文件",
		validators=[
			DataRequired("请上传文件!!")
		],
		description='文件',
	)

	info = TextAreaField(
		label="简介",
		validators=[
			DataRequired("请输入简介")
		],
		description='简介',
		render_kw={
			"class":"form-control",
			"row":10
		}
	)

	logo = FileField(
		label="封面",
		validators=[
			DataRequired("请上传封面!!")
		],
		description='封面',
	)

	star = SelectField(
		label="星级",
		validators=[
			DataRequired("请选择星际！")
		],
		description='星级',
		coerce=int,
		choices=[(1,'1星'),(2,'2星'),(3,'3星'),(4,'4星'),(5,'5星')],
		render_kw={
			"class":"form-control",
			"row":10
		}
	)

	tag_id = SelectField(
		label="标签",
		validators=[
			DataRequired("请选择标签！")
		],
		description='星级',
		coerce=int,
		choices=[(v.id,v.name) for v in tags],
		render_kw={
			"class":"form-control"
		}
	)

	area = StringField(
		label="地区",
		validators=[
			DataRequired("请输入地区!!!")
		],
		description='地区',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入地区！"
		}
	)

	length = StringField(
		label="片长",
		validators=[
			DataRequired("请输入片长")
		],
		description='片长',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入片长"
		}
	)

	release_time = StringField(
		label="上映时间",
		validators=[
			DataRequired("请选择上映时间")
		],
		description='上映时间',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入片长",
			"id":"input_release_time"
		}
	)

	submit = SubmitField(
		label="添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)


class PreviewForm(FlaskForm):

	title = StringField(
		label="预告名称",
		validators=[
			DataRequired("请输入预告名称")
		],
		description='预告名称',
		render_kw={
			"class":"form-control",
			"placeholder":"请输入预告名称"
		}
	)

	logo = FileField(
		label="封面",
		validators=[
			DataRequired("请上传封面!!")
		],
		description='封面',
	)

	submit = SubmitField(
		label="添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)



class AdminForm(FlaskForm):
	# 管理员登录表单
	name = StringField(
		"账号",
		validators=[
			DataRequired("请输入账号！！！")
		],
		description="账号",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入账号！!!",
			#"required":"required"
		}
	)

	pwd = PasswordField(
		"密码",
		validators=[
			DataRequired("请输入密码！!!")
		],
		description="密码",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入密码！!!",
			#"required":"required"
		}
	)

	role_id = SelectField(
		label="角色",
		validators=[
			DataRequired("请选择角色！")
		],
		description='角色',
		coerce=int,
		choices=[(1,'普通管理员'),(2,'超级管理员')],
		render_kw={
			"class":"form-control",
			"row":10
		}
	)

	submit = SubmitField(
		"登录",
		render_kw={
			"class":"btn btn-primary",
		}
	)

class MoviecolForm(FlaskForm):
	content = StringField(
		"收藏内容",
		validators=[
			DataRequired("请输入收藏内容！！！")
		],
		description="收藏内容",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入收藏内容！!!",
			#"required":"required"
		}
	)

	submit = SubmitField(
		label="添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)

class AuthForm(FlaskForm):
	name = StringField(
		"权限名称",
		validators=[
			DataRequired("请输入权限名称")
		],
		description="权限名称",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入权限名称!!",
			#"required":"required"
		}
	)

	submit = SubmitField(
		"添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)


class UserForm(FlaskForm):
	# 管理员登录表单
	name = StringField(
		"账号",
		validators=[
			DataRequired("请输入账号！！！")
		],
		description="账号",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入账号！!!",
			#"required":"required"
		}
	)

	pwd = PasswordField(
		"密码",
		validators=[
			DataRequired("请输入密码！!!")
		],
		description="密码",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入密码！!!",
			#"required":"required"
		}
	)

	submit = SubmitField(
		"添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)



class RoleForm(FlaskForm):
	name = StringField(
		"角色名称",
		validators=[
			DataRequired("请输入角色名称")
		],
		description="角色名称",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入角色名称!!",
			#"required":"required"
		}
	)

	auth_id = SelectField(
		label="标签",
		validators=[
			DataRequired("请选择权限！")
		],
		description='星级',
		coerce=int,
		choices=[(v.id,v.name) for v in tags],
		render_kw={
			"class":"form-control"
		}
	)

	submit = SubmitField(
		"添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)
class PwdForm(FlaskForm):
	old_pwd = StringField(
		label="旧密码",
		validators=[
			DataRequired("请输入旧密码")
		],
		description="旧密码",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入旧密码!!",
			#"required":"required"
		}
	)

	new_pwd = StringField(
		label="新密码",
		validators=[
			DataRequired("请输入新密码")
		],
		description="新密码",
		render_kw={
			"class":"form-control",
			"placeholder":"请输入新密码!!",
			#"required":"required"
		}
	)

	submit = SubmitField(
		label="添加",
		render_kw={
			"class":"btn btn-primary",
		}
	)

	def yalidata_old_pwd(self,field):
		from flask import session
		pwd = field.data
		name = session['admin']
		admin = Admin.query.filter_by(name=name).first()
		if not Admin.check_pwd(pwd):
			raise ValidationError("旧密码错误！")
