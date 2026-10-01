from flask_app import app
# Importamos los controladores para registrar todas las rutas de la aplicación
from flask_app.controllers import usuarios, libros

if __name__ == "__main__":
    app.run(debug=True)