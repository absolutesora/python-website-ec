from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from app.models import User
from flask_babel import _, lazy_gettext as _l


class LoginForm(FlaskForm):
    username = StringField(_l('Username', validators=[DataRequired()]))
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username', validators=[DataRequired()]))
    email = StringField(_l('Email', validators=[DataRequired(), Email()]))
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    password2 = PasswordField(_l('Confirm Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('Register'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first() # first function return 1 (found it) or None
        if user is not None:
            raise ValidationError(_('The username already exists. Please use a different username'))

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_('The Email already exists. Please use a different email address'))


class EditProfileForm(FlaskForm):
    about_me = TextAreaField(_l('About Me', validators=[Length(min=0, max=140)]))
    submit = SubmitField(_l('Change'))

class PostForm(FlaskForm):
    post = TextAreaField(_l('Tweet something', validators=[DataRequired(), Length(min=1, max=140)]))
    submit = SubmitField(_l('Tweet!'))


class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email', validators=[DataRequired(), Email()]))
    submit = SubmitField(_l('Password Reset'))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password', validators=[DataRequired()]))
    password2 = PasswordField(_l('Confirm Password', validators=[DataRequired(), EqualTo('password')]))
    submit = SubmitField(_l('Reset Password'))
