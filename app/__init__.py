from flask import Flask, render_template
from flask_login import LoginManager
from .config  import Config
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy    
from .mi_blueprint import mi_blueprint
from app.productos import productos
from app.clientes import clientes
from app.auth import auth
from flask_bootstrap import Bootstrap

# Inicializa el objeto flask
app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = "/auth/login"

# Inicializa el objeto de SQLAlchemy
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Registra modulos(Blueprints)
app.register_blueprint(mi_blueprint)
app.register_blueprint(productos)
app.register_blueprint(clientes)
app.register_blueprint(auth)

from .models import Cliente, Venta, Producto, Detalle

@app.route("/prueba")
def prueba():
    return render_template("base.html")

