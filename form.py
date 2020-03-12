from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,TextAreaField
from wtforms.validators import DataRequired

class MyForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    text = TextAreaField('Text')
    submit = SubmitField('Sign In')