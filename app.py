from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
import mariadb

app = Flask(__name__)
@app.route("/albums")
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


@app.route("/artistas")
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


@app.route("/canciones")
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


@app.route("/miembros")
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

@app.route("/rol")
def listar_roles():
        connection = mysql.connector.connect(
            host='10.9.120.5', 
            database='realdata',
            user='realdata',
            password='realdata111'
        )
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Roles")
        filas = cursor.fetchall()
        return jsonify(filas)


#------------------------------------------------------------

@app.route("/miembros/<int:id>", methods=("DELETE",))
def borrarMiembro(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Miembros WHERE id_miembro = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


@app.route("/artistas/<int:id>", methods=("DELETE",))
def borrarArtista(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Artistas WHERE id_Artista = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


@app.route("/canciones/<int:id>", methods=("DELETE",))
def borrarCancion(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Canciones WHERE id_canciones = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }



@app.route("/pais/<int:id>", methods=("DELETE",))
def borrarPais(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Pais WHERE nombre_pais = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }



@app.route("/roles/<int:id>", methods=("DELETE",))
def borrarRoles(id):
    connection = mysql.connector.connect(
        host='10.9.120.5', 
        database='realdata',
        user='realdata',
        password='realdata111'
    )
    cursor = connection.cursor()
    cursor.execute("DELETE FROM Roles WHERE nombre_rol = %s", (id,))
    connection.commit()
    cursor.close()
    connection.close()
    
    return { "resultado": "ok", "id": id }


#-----------------------------------------------------


@app.route("/albums/<int:id>")
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


@app.route("/artistas/<int:id>")
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


@app.route("/canciones/<int:id>")
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


@app.route("/miembros/<int:id>")
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


@app.route("/roles/<int:id>")
def detalle_Roles(id):
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

@app.route("/pais/<int:id>")
def detalle_pais(id):
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


#--------------------------------------------------------------

@app.route("/Albums/", methods=('POST',))
def agregar_Albums():
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    id_artista = request.json["id_artista"]
    titulo = request.json["titulo"]
    Año_lanzamiento = request.json["Año_lanzamiento"]
    genero = request.json["genero"]
    consulta = """
        INSERT INTO Albums (id_artista, titulo, Año_lanzamiento, genero)
        VALUES (%s, %s, %s, %s)
"""
    cur.execute(consulta, (id_artista, titulo, Año_lanzamiento, genero, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})


@app.route("/artistas/", methods=('POST',))
def agregar_artistas():
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    biografia = request.json["biografia"]
    genero = request.json["genero"]
    consulta = """
        INSERT INTO Artistas (nombre, biografia, genero)
        VALUES (%s, %s, %s)
"""
    cur.execute(consulta, (nombre, biografia, genero))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})


@app.route("/canciones/", methods=('POST',))
def agregar_canciones():
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)  
    id_album = request.json["id_album"] 
    titulo = request.json["titulo"]
    duracion = request.json["duracion"]
    numero_pista = request.json["numero_pista"]
    fecha_lanzamiento = request.json["fecha_lanzamiento"]
    consulta = """
        INSERT INTO Canciones (id_album, titulo, duracion, numero_pista, fecha_lanzamiento)
        VALUES (%s, %s, %s, %s)
"""
    cur.execute(consulta, (id_album, titulo, duracion, numero_pista, fecha_lanzamiento, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})



@app.route("/miembro/", methods=('POST',))
def agregar_miembro():
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)  
    id_artista = request.json["id_artista"] 
    nombre = request.json["nombre"]
    consulta = """
        INSERT INTO Miembro (id_artista, nombre)
        VALUES (%s, %s, %s, %s)
"""
    cur.execute(consulta, (id_artista, nombre, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})


@app.route("/pais/", methods=('POST',))
def agregar_pais():
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)  
    nombre_pais = request.json["nombre_pais"] 
    consulta = """
        INSERT INTO Pais (nombre_pais, nombre)
        VALUES (%s, %s, %s, %s)
"""
    cur.execute(consulta, (nombre_pais, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})


@app.route("/roles/", methods=('POST',))
def agregar_roles():
    mari = mariadb.connect( 
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)  
    nombre_rol = request.json["nombre_rol"] 
    consulta = """
        INSERT INTO Roles (nombre_rol, nombre)
        VALUES (%s, %s, %s, %s)
"""
    cur.execute(consulta, (nombre_rol, id))
    mari.commit()
    id = cur.lastrowid

    return jsonify({"resultado" : "ok",
                    "id" : id})

#-----------------------------------------------------------------------

@app.route("/albums/<int:id>", methods=('PUT',))
def modificar_albums(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    id_artista = request.json["id_artista"]
    titulo = request.json["titulo"]
    Año_lanzamiento = request.json["Año_lanzamiento"]
    genero = request.json["genero"]
    consulta = """
        UPDATE Albums SET id_artista = %s, titulo =%s, Año_lanzamiento =%s,
        genero =%s, WHERE id = %s;
"""
    cur.execute(consulta, (id_artista, titulo, Año_lanzamiento, genero, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})



@app.route("/artistas/<int:id>", methods=('PUT',))
def modificar_Artistas(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    nombre = request.json["nombre"]
    genero = request.json["genero"]
    biografia = request.json["biografia"]
    consulta = """ 
        UPDATE Artistas SET nombre = %s, genero =%s, biografia =%s,
        genero =%s, WHERE id = %s;
"""
    cur.execute(consulta, (nombre, genero, biografia, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})


@app.route("/canciones/<int:id>", methods=('PUT',))
def modificar_Canciones(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    id_album = request.json["id_album"]
    titulo = request.json["titulo"]
    duracion = request.json["duracion"]
    numero_pista = request.json["numero_pista"]
    fecha_lanzamiento = request.json["fecha_lanzamiento"]
    consulta = """ 
        UPDATE Canciones SET id_album = %s, titulo =%s, duracion =%s,
        numero_pista =%s, fecha_lanzamiento =%s WHERE id = %s;
"""
    cur.execute(consulta, (id_album, titulo, duracion, numero_pista, fecha_lanzamiento, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})



@app.route("/miembros/<int:id>", methods=('PUT',))
def modificar_Miembros(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    id_artista = request.json["id_artista"],
    nombre = request.json["nombre"]
    consulta = """ 
        UPDATE Miembros SET id_artista = %s, nombre =%s, duracion =%s,
        WHERE id = %s;
"""
    cur.execute(consulta, (id_artista, nombre, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})



@app.route("/pais/<int:id>", methods=('PUT',))
def modificar_Pais(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    nombre_pais = request.json["nombre_pais"]
    consulta = """ 
        UPDATE Pais SET nombre_pais =%s,
        WHERE id = %s;
"""
    cur.execute(consulta, (nombre_pais, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})



@app.route("/roles/<int:id>", methods=('PUT',))
def modificar_Roles(id):
    mari = mariadb.connect(
        user = "realdata",
        password ="realdata111",
        host ="10.9.120.5",
        database= "realdata"
    )
    cur = mari.cursor(dictionary=True)
    nombre_rol = request.json["nombre_rol"]
    consulta = """ 
        UPDATE Roles SET nombre_rol =%s,
        WHERE id = %s;
"""
    cur.execute(consulta, (nombre_rol, id))    
    mari.commit()
    cur.close()
    mari.close()

    return jsonify({"resultado" : "ok",
                    "id" : id})