from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error
app = Flask(__name__)
@app.route("/Albums")
def listar_albums():
     # Conexión con los parámetros necesarios
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        cursor = connection.cursor(dictionary=True)
            # Ejecutar la consulta SQL
        cursor.execute("SELECT * FROM Albums")
            # Obtener nombres de las columnas
        filas = cursor.fetchall()
            # Formatear los resultados como una lista de diccionarios
        
        return jsonify(filas)


@app.route("/Artistas")
def listar_artistas():
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Artistas")
        filas = cursor.fetchall()
        return jsonify(filas)


@app.route("/Canciones")
def listar_canciones():
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Canciones")
        filas = cursor.fetchall()
        return jsonify(filas)


@app.route("/Miembros")
def listar_miembros():
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Miembros")
        filas = cursor.fetchall()
        return jsonify(filas)

#-------------------------------

@app.route("/miembros/<int:id>", methods=("DELETE",))
def borrarMiembro(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Miembros WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


@app.route("/Artistas/<int:id>", methods=("DELETE",))
def borrarArtista(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Artistas WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


@app.route("/Canciones/<int:id>", methods=("DELETE",))
def borrarCancion(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Canciones WHERE id = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


#-----------------------------------------------------


@app.route("/Albums/<int:id>")
def detalle_album(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items WHERE ID= ?", (id,))
    items = [column[0] for column in cur.description]
    
    tabla = [dict(zip(items, row)) for row in cur.fetchall()]
    return jsonify(tabla)


@app.route("/Artistas/<int:id>")
def detalle_artista(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items WHERE ID= ?", (id,))
    items = [column[0] for column in cur.description]
    
    tabla = [dict(zip(items, row)) for row in cur.fetchall()]
    return jsonify(tabla)


@app.route("/Canciones/<int:id>")
def detalle_cancion(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items WHERE ID= ?", (id,))
    items = [column[0] for column in cur.description]
    
    tabla = [dict(zip(items, row)) for row in cur.fetchall()]
    return jsonify(tabla)


@app.route("/Miembros/<int:id>")
def detalle_miembro(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor()
    cur.execute("SELECT * FROM items WHERE ID= ?", (id,))
    items = [column[0] for column in cur.description]
    
    tabla = [dict(zip(items, row)) for row in cur.fetchall()]
    return jsonify(tabla)