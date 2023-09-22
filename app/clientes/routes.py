from app.clientes import clientes
from flask import render_template, redirect, flash
from flask_login import login_required
import app
from .forms import NewClientForm, EditClientForm



@clientes.route('/crear' ,  methods = ['GET', 'POST'])
@login_required
def crear():
    
    cliente = app.models.Cliente()
    form = NewClientForm()
    if form.validate_on_submit():
        form.populate_obj(cliente),
        app.db.session.add(cliente),
        app.db.session.commit()
        flash("Cliente registrado correctamente")
        return redirect('/clientes/listar')
    return render_template('crearClient.html', form = form)

@clientes.route('/listar')
@login_required
def listar():
    clientes = app.models.Cliente.query.all()    
    return render_template("listarClient.html",
                           clientes = clientes)

@clientes.route('/eliminar/<cliente_id>')
@login_required
def eliminar(cliente_id):
    p = app.models.Cliente.query.get(cliente_id)
    if p:
        app.db.session.delete(p)
        app.db.session.commit()
        flash('Cliente eliminado')
    return redirect ('/clientes/listar')


@clientes.route('/editar/<cliente_id>', methods = ['GET', 'POST'])
@login_required
def editar(cliente_id):
    
    p = app.models.Cliente.query.get(cliente_id)
    form = EditClientForm(obj = p)
    
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Cliente actualizado')
        return redirect('/clientes/listar')
    return render_template("crearClient.html",
                           form = form)
        
    
