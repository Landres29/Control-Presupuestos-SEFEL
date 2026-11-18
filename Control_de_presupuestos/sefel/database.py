import sqlite3
import os


def obtener_conexion():
    ruta = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "sefel.db"
    )

    conexion = sqlite3.connect(ruta)
    return conexion


def crear_base_datos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS obras (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT
        )
    """)

    conexion.commit()
    conexion.close()


def agregar_obra(nombre, descripcion):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO obras (nombre, descripcion)
        VALUES (?, ?)
        """,
        (nombre, descripcion)
    )

    conexion.commit()
    conexion.close()


def obtener_obras():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT id, nombre, descripcion
        FROM obras
        ORDER BY id DESC
        """
    )

    obras = cursor.fetchall()

    conexion.close()
    return obras