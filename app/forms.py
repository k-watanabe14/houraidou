from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, DateField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional, NumberRange
from app.models import User
from werkzeug.security import check_password_hash


def check_unique_username(form, field):
    if User.query.filter_by(username=field.data).first():
        raise ValidationError('ユーザー名「 {} 」はすでに使用されています。'.format(field.data))

def check_unique_email(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('メールアドレス「 {} 」はすでに登録されています。'.format(field.data))

def exists_email(form, field):
    if not User.query.filter_by(email=field.data).first():
        raise ValidationError('メールアドレスが間違っています。正しいメールアドレスを入力してください。')

# ENHANCE: Change all frorms to WTForm
class SignupForm(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired(), check_unique_username])
    email = StringField('メールアドレス', validators=[DataRequired(), Email(message='有効なメールアドレスを入力してください。'), check_unique_email])
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=8, max=15, message='有効なパスワードを入力してください。')])
    submit = SubmitField('登録する')


class LoginFrom(FlaskForm):
    username = StringField('ユーザー名', validators=[DataRequired()])
    password = PasswordField('パスワード', validators=[DataRequired()])
    submit = SubmitField('ログインする')


class RequestResetForm(FlaskForm):
    email = StringField('メールアドレス', validators=[DataRequired(), exists_email])
    submit = SubmitField('パスワード再設定のメールを送る')


class ResetPasswordForm(FlaskForm):
    password = PasswordField('パスワード', validators=[DataRequired(), Length(min=8, max=15, message='有効なパスワードを入力してください。')])
    confirm_password = PasswordField('パスワード（確認用）', validators=[DataRequired(), EqualTo('password', message='パスワードとパスワード（確認用）に同じパスワードを設定してください。')])
    submit = SubmitField('パスワードを再設定する')


class RegisterBookForm(FlaskForm):
    ## FIXME: Allow to empty isbn
    isbn =  StringField('ISBN', validators=[Length(min=10, max=13, message='10桁もしくは13桁の数字を入力してください。')])
    title = StringField('タイトル', validators=[DataRequired()])
    author = StringField('著者')
    publisher_name = StringField('出版社')
    sales_date = StringField('出版年月日')
    image_url = StringField()
    borrower_id = IntegerField()
    checkout_date = DateField()