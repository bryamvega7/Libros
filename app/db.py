from pymongo import MongoClient

conexion = MongoClient()

conexion = MongoClient('localhost', 27017)

db = conexion['aula6_libros'] #bd nombre
