from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', render_kw={'placeholder': "Enter your e-mail here."}, validators=[DataRequired(), Email()])

    password = PasswordField('Password', validators=[DataRequired()])
    c_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password', message='Confirm Password must be equal to Password')])

    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()], render_kw={'placeholder': "Enter your e-mail here."})

    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember-me')
    submit = SubmitField('Sign Up')