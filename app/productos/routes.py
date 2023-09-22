from app.productos import productos
from flask import render_template, redirect, flash
from flask_login import login_required
from .forms  import NewProductForm, EditProductForm
import app
import os



@productos.route('/crear',  methods = ['GET', 'POST'])
@login_required
def crear():        
        producto = app.models.Producto()
        form = NewProductForm()
        if form.validate_on_submit():
            # Guarda el producto en la bd
            form.populate_obj(producto),
            producto.imagen = form.Imagen.data.filename
            app.db.session.add(producto),
            app.db.session.commit()
            #Subir imagen a /imagenes
            archivo = form.Imagen.data 
            archivo.save(os.path.abspath(os.getcwd() + "\\app\\productos\\imagenes\\"+ producto.imagen))
            flash("Producto registrado correctamente")
            return redirect('/productos/listar')
        return render_template('crearProduct.html', form = form)

@productos.route('/listar')
@login_required
def listar():
    productos = app.models.Producto.query.all()
    return render_template("listarProduct.html",
                           productos = productos)

@productos.route('/eliminar/<producto_id>')
@login_required
def eliminar(producto_id):
    
    p = app.models.Producto.query.get(producto_id)
    if p:
        app.db.session.delete(p)
        app.db.session.commit()
        flash('Producto eliminado')
    return redirect ('/productos/listar')


@productos.route('/editar/<producto_id>', methods = ['GET','POST'])
@login_required
def editar(producto_id):
    p = app.models.Producto.query.get(producto_id)
    form = EditProductForm(obj = p)
    if form.validate_on_submit():
        form.populate_obj(p)
        app.db.session.commit()
        flash('Producto actualizado')
        return redirect('/productos/listar')
    return render_template("crearProduct.html", 
                           form = form)

