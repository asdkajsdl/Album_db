from flask import Flask, jsonify, render_template, request
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Función para obtener conexión a la base de datos
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        return connection
    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None

# Función para ejecutar una consulta SQL y devolver los resultados
def fetch_data(query, params=None):
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    cursor = connection.cursor(dictionary=True)
    try:
        cursor.execute(query, params or ())
        rows = cursor.fetchall()
        return rows
    except Error as e:
        print(f"Error al ejecutar la consulta: {e}")
        return jsonify({"error": "Error en la consulta SQL"}), 500
    finally:
        cursor.close()
        connection.close()

# Ruta principal con un enlace a las demás secciones
@app.route("/")
def home():
    return render_template('index.html')

# ------------------------- Rutas para obtener listas de datos ---------------------------

@app.route("/albums")
def listar_albums():
    query = "SELECT * FROM Albums"
    albums = fetch_data(query)
    return render_template('albums.html', albums=albums)

@app.route("/artistas")
def listar_artistas():
    query = "SELECT * FROM Artistas"
    artistas = fetch_data(query)
    return render_template('artistas.html', artistas=artistas)

@app.route("/canciones")
def listar_canciones():
    query = "SELECT * FROM Canciones"
    canciones = fetch_data(query)
    return render_template('canciones.html', canciones=canciones)

@app.route("/miembros")
def listar_miembros():
    query = "SELECT * FROM Miembros"
    miembros = fetch_data(query)
    return render_template('miembros.html', miembros=miembros)

@app.route("/roles")
def listar_roles():
    query = "SELECT * FROM Roles"
    roles = fetch_data(query)
    return render_template('roles.html', roles=roles)

# ------------------------- Rutas para crear nuevos registros ---------------------------

@app.route("/albums", methods=["POST"])
def crear_album():
    data = request.get_json()
    nombre = data.get("nombre")
    artista_id = data.get("artista_id")
    fecha_lanzamiento = data.get("fecha_lanzamiento")

    query = """
        INSERT INTO Albums (nombre, artista_id, fecha_lanzamiento)
        VALUES (%s, %s, %s)
    """
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, (nombre, artista_id, fecha_lanzamiento))
        connection.commit()
        return jsonify({"resultado": "ok", "nombre": nombre})
    except Error as e:
        print(f"Error al crear álbum: {e}")
        return jsonify({"error": "Error al crear álbum"}), 500
    finally:
        cursor.close()
        connection.close()

# ------------------------- Rutas para eliminar registros ---------------------------

@app.route("/albums/<int:id>", methods=["DELETE"])
def borrar_album(id):
    query = "DELETE FROM Albums WHERE id_album = %s"
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, (id,))
        connection.commit()
        return jsonify({"resultado": "ok", "id": id})
    except Error as e:
        print(f"Error al borrar álbum: {e}")
        return jsonify({"error": "Error al borrar álbum"}), 500
    finally:
        cursor.close()
        connection.close()

# ------------------------- Rutas para modificar registros ---------------------------

@app.route("/albums/<int:id>", methods=["PUT"])
def modificar_album(id):
    data = request.get_json()
    nombre = data.get("nombre")
    artista_id = data.get("artista_id")
    fecha_lanzamiento = data.get("fecha_lanzamiento")

    query = """
        UPDATE Albums
        SET nombre = %s, artista_id = %s, fecha_lanzamiento = %s
        WHERE id_album = %s
    """
    connection = get_db_connection()
    if connection is None:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    cursor = connection.cursor()
    try:
        cursor.execute(query, (nombre, artista_id, fecha_lanzamiento, id))
        connection.commit()
        return jsonify({"resultado": "ok", "id": id})
    except Error as e:
        print(f"Error al modificar álbum: {e}")
        return jsonify({"error": "Error al modificar álbum"}), 500
    finally:
        cursor.close()
        connection.close()

# ------------------------- Otras Rutas de CRUD ---------------------------

# Similar para las tablas Artistas, Canciones, Miembros y Roles:
# Asegúrate de definir las rutas de **POST**, **DELETE**, **PUT** para cada tabla.
# Puedes seguir el patrón mostrado en las rutas anteriores.

if __name__ == "__main__":
    app.run(debug=True)
