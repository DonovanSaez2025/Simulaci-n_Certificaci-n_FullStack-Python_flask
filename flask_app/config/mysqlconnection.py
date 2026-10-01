# Importaciones
import pymysql
import pymysql.cursors
import os

# Clase para conectarse a la base de datos
class MySQLConnection:
    def __init__(self, db):
        self.db = db

    # Parámetros de la conexión
    def query_db(self, query, data=None):
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=self.db,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True)
        
        # Intentar conectarse
        with connection.cursor() as cursor:
            try:
                cursor.execute(query, data or {})
                if query.strip().lower().startswith("select"):
                    return cursor.fetchall()
                return cursor.lastrowid
            except Exception as e:
                print(f"Error MySQL: {e}")
                return False
            finally:
                connection.close()
                
def connectToMySQL(db):
    return MySQLConnection(db)