from app.auth import auth
from flask import render_template, redirect, flash
import app
from .forms import LoginForm
from flask_login import login_user, current_user, logout_user

@auth.route('/login',
            methods = ['GET', 'POST'])
def login (): 
    form = LoginForm()
    if form.validate_on_submit():
        #Selecciona al cliente por 
        #username
        c = app.models.Cliente.query.filter_by(username = form.username.data).first()
        if c is None or not c.check_password(form.password.data):
            flash("Usuario no existente o clave incorrecta")
            return redirect('/auth/login')
        else:
            login_user(c, remember= True)
            flash("Logueado con exito")
            return redirect('/productos/listar')
    return render_template('login.html', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect('/auth/login')
    
