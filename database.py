import sqlite3
from dolar import obtener_dolar_blue
from datetime import datetime





conexion = sqlite3.connect("dolar.db")
cursor = conexion.cursor()



def creacion_tabla():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotizaciones (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               fuente TEXT,
               precio REAL,
               fecha TEXT
               
               
               )
    """)
    conexion.commit()

def guardar_cotizacion():
    fecha = datetime.now().isoformat()
    venta_blue = obtener_dolar_blue()
    cursor.execute("""
               INSERT INTO cotizaciones (fuente, precio, fecha)
               VALUES (?, ?, ?)
               """, ("Blue",  venta_blue , fecha))

    conexion.commit()

def mostrar_cotizacion():
    cursor.execute("SELECT * FROM cotizaciones")
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)


if __name__ == "__main__":
    creacion_tabla()
    guardar_cotizacion()
    mostrar_cotizacion()