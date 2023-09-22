from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField
from wtforms.validators import InputRequired, Length, Email
from flask_wtf.file import *

class ClienteForm(FlaskForm):
    username = StringField("Ingrese Nombre", validators=[InputRequired(message="Llenar campo")])
    password = StringField("Ingrese Contraseña",
                          validators=[
                              InputRequired(message="Llenar campo"),
                              Length(min=8, max=20, message="Contraseña consta de 8 a 20 caracteres")
                          ])
    email = EmailField("Ingrese correo electrónico",
                       validators=[
                           InputRequired(message="Correo obligatorio"),
                           Email(message="Debe ser un correo electrónico válido")
                       ])

class NewClientForm(ClienteForm):
    submit = SubmitField("Crear")

class EditClientForm(ClienteForm):
    submit = SubmitField("Actualizar Cliente")
