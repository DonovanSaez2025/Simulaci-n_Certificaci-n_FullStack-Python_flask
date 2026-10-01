# Importaciones
import re
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL

# Filtro de caracteres en los email
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Clase Usuario
class Usuario:
    # Método constructor
    def __init__(self, data):
        self.id = data["id"]
        self.nombre = data["nombre"]
        self.apellido = data["apellido"]
        