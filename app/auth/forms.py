from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, PasswordField


class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario:")
    password = PasswordField("Contraseña:")
    submit = SubmitField("Iniciar sesión")