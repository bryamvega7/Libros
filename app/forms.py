from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,DateField,TextAreaField,SubmitField
from wtforms.validators import DataRequired

class LibroForm(FlaskForm):
    titulo =StringField('Titulo : ',validators=[DataRequired()])
    autor =StringField('Autor : ',validators=[DataRequired()])
    pagina =IntegerField('Pagina : ',validators=[DataRequired()])
    fecha_publicacion =DateField('Fecha de publicacion : ',validators=[DataRequired()])
    descripcion =TextAreaField('Descripcion: ',validators=[DataRequired()])
    isbn=StringField('ISBN : ',validators=[DataRequired()])
    boton = SubmitField("Guardar Libro")
