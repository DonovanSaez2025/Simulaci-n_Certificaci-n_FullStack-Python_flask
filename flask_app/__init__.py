from flask import Flask

app = Flask(__name__)
# Clave secreta requerida para manejar sesiones y mensajes flash en Flask
app.secret_key = "clave_secreta_certificacion"