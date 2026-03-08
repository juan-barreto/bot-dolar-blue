import sqlite3
from dolar import *
from datetime import datetime





conexion = sqlite3.connect("dolar.db")
cursor = conexion.cursor()



def creacion_tabla():
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS cotizaciones (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               fuente TEXT,
               venta REAL,
               compra REAL,
               fecha TEXT
               
               
               )
    """)
    conexion.commit()

def guardar_cotizacion(fuente,venta,compra):
    fecha = datetime.now().isoformat()

    cursor.execute("""
               INSERT INTO cotizaciones (fuente, venta, compra, fecha)
               VALUES (?, ?, ?, ?)
               """, (fuente, venta, compra, fecha))

    conexion.commit()

def mostrar_cotizacion():
    cursor.execute("SELECT * FROM cotizaciones")
    resultados = cursor.fetchall()

    for fila in resultados:
        print(fila)


if __name__ == "__main__":
    creacion_tabla()
    mostrar_cotizacion()