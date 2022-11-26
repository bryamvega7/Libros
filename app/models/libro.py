import datetime

class Libro:
    def __init__(self,titulo,autor,pagina,fecha_publicacion,descripcion,isbn):
        self.titulo = titulo
        self.autor = autor
        self.pagina = pagina
        self.fecha_publicacion = fecha_publicacion
        self.descripcion = descripcion
        self.isbn = isbn
        
    def to_json(self):
        return{
            'titulo':self.titulo,
            'autor':self.autor,
            'pagina':self.pagina,
            'fecha_publicacion':datetime.datetime.strptime(str(self.fecha_publicacion),"%Y-%m-%d"),
            'descripcion':self.descripcion,
            'isbn':self.isbn
        }
