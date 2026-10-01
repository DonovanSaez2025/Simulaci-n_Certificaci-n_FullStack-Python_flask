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
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    # Validar datos del usuario
    @staticmethod
    def validacion(datos):
        valido = True
        
        # Validar nombre
        if not datos["nombre"].strip():
            flash("El nombre es obligatorio.", "nombre")
            valido = False
        elif len(datos["nombre"].strip()) < 2:
            flash("El nombre debe tener al menos 2 caracteres.", "nombre")
            valido = False
            
        # Validar apellido
        if not datos["apellido"].strip():
            flash("El apellido es obligatorio.", "apellido")
            valido = False
        elif len(datos["apellido"].strip()) < 2:
            flash("El apellido debe tener al menos 2 caracteres.", "apellido")
            valido = False
            
        # Validar email
        if not datos["email"].strip():
            flash("El email es obligatorio.", "email")
            es_valido = False
        elif not EMAIL_REGEX.match(datos["email"].strip()):
            flash("El email no tiene un formato válido.", "email")
            es_valido = False
            
        # Validar contraseña
        if not datos["password_hash"]:
            flash("La contraseña es obligatoria.", "password_hash")
            es_valido = False
        elif len(datos["password_hash"]) < 8:
            flash("La contraseña debe tener al menos 8 caracteres.", "password_hash")
            es_valido = False
            
        # Validar que ambas contraseñas sean iguales
        if datos["password_hash"] != datos["conf_password"]:
            flash("Las contraseñas no coinciden.", "password_hash")
            es_valido = False