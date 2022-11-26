from flask import Blueprint,render_template,redirect,url_for
from app.forms import LibroForm
from app.models.libro import Libro
from app.db import db

#ruta
libros_ruta = Blueprint('libros_ruta',__name__)

@libros_ruta.route('/') #Mostrar la tabla
def index():
    libros = db.libro.find()
    return render_template('index.html',libros=libros)

@libros_ruta.route('/crear-libro',methods=['POST','GET']) #Crear un libro
def guardar_libro():
    form_obj = LibroForm()
    
    if form_obj.validate_on_submit():
        nuevo_libro = Libro(form_obj.titulo.data,
                            form_obj.autor.data,
                            form_obj.pagina.data,
                            form_obj.fecha_publicacion.data,
                            form_obj.descripcion.data,
                            form_obj.isbn.data)
        
        db.libro.insert_one(nuevo_libro.to_json())
        
        return redirect(url_for('libros_ruta.index'))

    
    return render_template('guardar_libro.html', form_obj=form_obj)