import sqlite3
import os


def obtener_ruta_base_datos():
    return os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "sefel.db"
    )


def base_datos_existe():
    ruta = obtener_ruta_base_datos()
    return os.path.exists(ruta)


def obtener_conexion():
    ruta = obtener_ruta_base_datos()

    if not os.path.exists(ruta):
        raise FileNotFoundError(
            "No se encontró la base de datos sefel.db."
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

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS presupuestos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            obra_id INTEGER NOT NULL,
            partida TEXT NOT NULL,
            monto REAL NOT NULL,
            FOREIGN KEY (obra_id) REFERENCES obras(id)
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            obra_id INTEGER NOT NULL,
            partida TEXT NOT NULL,
            concepto TEXT NOT NULL,
            monto REAL NOT NULL,
            fecha TEXT NOT NULL,
            FOREIGN KEY (obra_id) REFERENCES obras(id)
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


def agregar_presupuesto(obra_id, partida, monto):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO presupuestos (obra_id, partida, monto)
        VALUES (?, ?, ?)
        """,
        (obra_id, partida, monto)
    )

    conexion.commit()
    conexion.close()


def obtener_presupuestos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            presupuestos.id,
            obras.nombre,
            presupuestos.partida,
            presupuestos.monto
        FROM presupuestos
        INNER JOIN obras
            ON presupuestos.obra_id = obras.id
        ORDER BY presupuestos.id DESC
        """
    )

    presupuestos = cursor.fetchall()

    conexion.close()
    return presupuestos


def obtener_total_presupuesto_obra(obra_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(monto), 0)
        FROM presupuestos
        WHERE obra_id = ?
        """,
        (obra_id,)
    )

    total = cursor.fetchone()[0]

    conexion.close()
    return total


def agregar_gasto(obra_id, partida, concepto, monto, fecha):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO gastos (
            obra_id,
            partida,
            concepto,
            monto,
            fecha
        )
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            obra_id,
            partida,
            concepto,
            monto,
            fecha
        )
    )

    conexion.commit()
    conexion.close()


def obtener_gastos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT
            gastos.id,
            obras.nombre,
            gastos.partida,
            gastos.concepto,
            gastos.monto,
            gastos.fecha
        FROM gastos
        INNER JOIN obras
            ON gastos.obra_id = obras.id
        ORDER BY gastos.id DESC
        """
    )

    gastos = cursor.fetchall()

    conexion.close()
    return gastos


def obtener_total_gastos_obra(obra_id):
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT COALESCE(SUM(monto), 0)
        FROM gastos
        WHERE obra_id = ?
        """,
        (obra_id,)
    )

    total = cursor.fetchone()[0]

    conexion.close()
    return total


def obtener_resumen_costos():
    conexion = obtener_conexion()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT
            obras.id,
            obras.nombre,

            COALESCE(
                (
                    SELECT SUM(p.monto)
                    FROM presupuestos p
                    WHERE p.obra_id = obras.id
                ),
                0
            ) AS presupuesto,

            COALESCE(
                (
                    SELECT SUM(g.monto)
                    FROM gastos g
                    WHERE g.obra_id = obras.id
                ),
                0
            ) AS gastos

        FROM obras

        ORDER BY obras.id DESC
    """)

    datos = cursor.fetchall()

    conexion.close()
    return datos