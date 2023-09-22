from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField 
from wtforms.validators import InputRequired, NumberRange
from flask_wtf.file import *

class ProductForm():
    nombre = StringField("Ingrese el nombre del producto", 
                         validators = [InputRequired( message = "Llenar campo" )])
    precio = IntegerField("Ingrese el precio del producto",
                          validators = [InputRequired( message = "Llenar campo"),
                          NumberRange (min = 10000,
                                      max = 100000,
                                      message = "Bajale o Subile")])

class NewProductForm(FlaskForm, ProductForm):
    Imagen = FileField(label = "Imagen",
                       validators = [
                           FileRequired(message = "Imagen obligatoria"),
                            FileAllowed (
                                ["jpg","png","jpeg"], 
                                message = "Formato invalido"
                            )
                       ])
    submit = SubmitField("Crear")


class EditProductForm(FlaskForm, ProductForm):
    submit = SubmitField("Actualizar")