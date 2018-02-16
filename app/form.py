from flask import Flask, render_template, flash, session, redirect, url_for
from wtforms import TextAreaField
from flask_wtf import FlaskForm
from flask_wtf.recaptcha import RecaptchaField

from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField
from wtforms.validators import DataRequired, Email

DEBUG = True
SECRET_KEY = 'secret'

# keys for localhost. Change as appropriate.

app = Flask(__name__)
app.config.from_object(__name__)

class MyForm(FlaskForm):
    firstname = StringField('First Name', validators=[DataRequired()])
    lastname = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subject = StringField('Subject', validators=[DataRequired()])
    message= TextAreaField("Message", validators=[DataRequired()])

if __name__ == "__main__":
    app.run()