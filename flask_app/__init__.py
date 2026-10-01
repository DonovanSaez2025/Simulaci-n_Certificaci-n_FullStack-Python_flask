from flask import Flask
import os

app = Flask(__name__)
# Clave secreta requerida para manejar sesiones y mensajes flash en Flask
app.secret_key = os.getenv("SECRET_KEY")